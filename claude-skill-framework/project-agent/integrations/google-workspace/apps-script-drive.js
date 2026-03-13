/**
 * Google Apps Script for Drive Integration
 * Project-Agent Automation Scripts
 * 
 * Copy this to Google Apps Script (script.google.com)
 * Free-tier compatible
 */

// ==================== FOLDER MANAGEMENT ====================

/**
 * Create project folder structure
 * @param {string} projectName - Name of the project
 * @return {object} Folder IDs
 */
function createProjectFolders(projectName) {
  var rootFolder = DriveApp.createFolder(projectName + " - Internship Project");
  var folderIds = { root: rootFolder.getId() };
  
  var folders = [
    { key: "planning", name: "01 - Planning Documents" },
    { key: "content", name: "02 - Content & Calendar" },
    { key: "reports", name: "03 - Reports & Analytics" },
    { key: "templates", name: "04 - Templates" },
    { key: "risk", name: "05 - Risk & Issue Management" }
  ];
  
  folders.forEach(function(folder) {
    var subFolder = rootFolder.createFolder(folder.name);
    folderIds[folder.key] = subFolder.getId();
  });
  
  return folderIds;
}

/**
 * Get or create folder by path
 * @param {string} path - Folder path
 * @return {Folder} Google Drive folder
 */
function getOrCreateFolder(path) {
  var parts = path.split("/").filter(function(p) { return p; });
  var folder = DriveApp.getRootFolder();
  
  parts.forEach(function(part) {
    var folders = folder.getFoldersByName(part);
    if (folders.hasNext()) {
      folder = folders.next();
    } else {
      folder = folder.createFolder(part);
    }
  });
  
  return folder;
}

// ==================== FILE OPERATIONS ====================

/**
 * Upload markdown file to Drive folder
 * @param {string} folderId - Target folder ID
 * @param {string} fileName - File name
 * @param {string} content - File content
 * @return {File} Created file
 */
function uploadMarkdownFile(folderId, fileName, content) {
  var folder = DriveApp.getFolderById(folderId);
  var blob = Utilities.newBlob(content, 'text/plain', fileName);
  return folder.createFile(blob);
}

/**
 * Convert markdown content to Google Doc
 * @param {string} folderId - Target folder ID
 * @param {string} title - Document title
 * @param {string} content - Markdown content
 * @return {File} Created Google Doc file
 */
function convertToGoogleDoc(folderId, title, content) {
  var folder = DriveApp.getFolderById(folderId);
  
  // Create Google Doc
  var doc = DocumentApp.create(title);
  var body = doc.getBody();
  
  // Parse and add content
  var lines = content.split("\n");
  lines.forEach(function(line) {
    if (line.startsWith("# ")) {
      body.appendParagraph(line.substring(2)).setHeading(DocumentApp.ParagraphHeading.HEADING1);
    } else if (line.startsWith("## ")) {
      body.appendParagraph(line.substring(3)).setHeading(DocumentApp.ParagraphHeading.HEADING2);
    } else if (line.startsWith("### ")) {
      body.appendParagraph(line.substring(4)).setHeading(DocumentApp.ParagraphHeading.HEADING3);
    } else if (line.startsWith("- ") || line.startsWith("* ")) {
      body.appendListItem(line.substring(2));
    } else if (line.trim() !== "") {
      body.appendParagraph(line);
    }
  });
  
  doc.saveAndClose();
  
  // Move to target folder
  var docFile = DriveApp.getFileById(doc.getId());
  folder.addFile(docFile);
  DriveApp.getRootFolder().removeFile(docFile);
  
  return docFile;
}

// ==================== GOOGLE SHEETS ====================

/**
 * Create KPI Dashboard spreadsheet
 * @param {string} folderId - Target folder ID
 * @param {string} projectName - Project name
 * @return {Spreadsheet} Created spreadsheet
 */
function createKPIDashboard(folderId, projectName) {
  var folder = DriveApp.getFolderById(folderId);
  var ss = SpreadsheetApp.create(projectName + " - KPI Dashboard");
  
  // Dashboard sheet
  var dashboard = ss.getActiveSheet();
  dashboard.setName("Dashboard");
  
  // Headers
  var headers = ["KPI Name", "Category", "Target", "Current", "Progress %", "Status", "Owner", "Due Date"];
  dashboard.getRange(1, 1, 1, headers.length).setValues([headers]);
  dashboard.getRange(1, 1, 1, headers.length).setFontWeight("bold").setBackground("#4285f4").setFontColor("white");
  
  // Sample data
  var sampleData = [
    ["Social Media Followers", "Social Media", 10000, 0, "", "", "", ""],
    ["Content Articles", "Content", 20, 0, "", "", "", ""],
    ["Engagement Rate", "Social Media", 5.0, 0, "", "", "", ""]
  ];
  dashboard.getRange(2, 1, sampleData.length, sampleData[0].length).setValues(sampleData);
  
  // Formulas
  dashboard.getRange("E2:E" + (sampleData.length + 1)).setFormulaR1C1("=IF(RC[-2]>0,ROUND(RC[-1]/RC[-2]*100,1),0)");
  dashboard.getRange("F2:F" + (sampleData.length + 1)).setFormulaR1C1('=IF(RC[-1]>=100,"Complete",IF(RC[-1]>=75,"On Track",IF(RC[-1]>=50,"At Risk","Behind")))');
  
  // Conditional formatting
  var statusRange = dashboard.getRange("F2:F100");
  var rules = [
    SpreadsheetApp.newConditionalFormatRule().whenTextEqualTo("Complete").setBackground("#00ff00").setRanges([statusRange]).build(),
    SpreadsheetApp.newConditionalFormatRule().whenTextEqualTo("On Track").setBackground("#ffff00").setRanges([statusRange]).build(),
    SpreadsheetApp.newConditionalFormatRule().whenTextEqualTo("At Risk").setBackground("#ff9900").setRanges([statusRange]).build(),
    SpreadsheetApp.newConditionalFormatRule().whenTextEqualTo("Behind").setBackground("#ff0000").setRanges([statusRange]).build()
  ];
  dashboard.setConditionalFormatRules(rules);
  
  // Weekly Tracking sheet
  var tracking = ss.insertSheet("Weekly Tracking");
  tracking.getRange(1, 1, 1, 5).setValues([["Week", "Date", "KPI", "Value", "Notes"]]);
  
  // Summary sheet
  var summary = ss.insertSheet("Summary");
  summary.getRange(1, 1, 6, 2).setValues([
    ["Metric", "Value"],
    ["Total KPIs", "=COUNTA(Dashboard!A:A)-1"],
    ["Completed", '=COUNTIF(Dashboard!F:F,"Complete")'],
    ["On Track", '=COUNTIF(Dashboard!F:F,"On Track")'],
    ["At Risk", '=COUNTIF(Dashboard!F:F,"At Risk")'],
    ["Behind", '=COUNTIF(Dashboard!F:F,"Behind")']
  ]);
  
  // Move to folder
  var file = DriveApp.getFileById(ss.getId());
  folder.addFile(file);
  DriveApp.getRootFolder().removeFile(file);
  
  return ss;
}

/**
 * Create Content Calendar spreadsheet
 * @param {string} folderId - Target folder ID
 * @param {string} projectName - Project name
 * @return {Spreadsheet} Created spreadsheet
 */
function createContentCalendar(folderId, projectName) {
  var folder = DriveApp.getFolderById(folderId);
  var ss = SpreadsheetApp.create(projectName + " - Content Calendar");
  
  var calendar = ss.getActiveSheet();
  calendar.setName("Content Calendar");
  
  var headers = ["ID", "Title", "Type", "Status", "Author", "Due Date", "Publish Date", "Platform", "Keywords", "Notes"];
  calendar.getRange(1, 1, 1, headers.length).setValues([headers]);
  calendar.getRange(1, 1, 1, headers.length).setFontWeight("bold").setBackground("#4285f4").setFontColor("white");
  
  // Data validation for Type
  var typeValidation = SpreadsheetApp.newDataValidation().requireValueInList(["Article", "Social Media", "Video", "Infographic", "Report"]).build();
  calendar.getRange("C2:C1000").setDataValidation(typeValidation);
  
  // Data validation for Status
  var statusValidation = SpreadsheetApp.newDataValidation().requireValueInList(["Planned", "In Progress", "Review", "Published", "Cancelled"]).build();
  calendar.getRange("D2:D1000").setDataValidation(statusValidation);
  
  // Move to folder
  var file = DriveApp.getFileById(ss.getId());
  folder.addFile(file);
  DriveApp.getRootFolder().removeFile(file);
  
  return ss;
}

// ==================== SHARING ====================

/**
 * Share folder with team members
 * @param {string} folderId - Folder ID
 * @param {Array} emails - Array of email addresses
 * @param {string} role - Role (viewer, editor, commenter)
 */
function shareFolder(folderId, emails, role) {
  var folder = DriveApp.getFolderById(folderId);
  
  emails.forEach(function(email) {
    folder.addEditor(email);
  });
}

// ==================== MAIN SETUP ====================

/**
 * Main setup function - creates complete project structure
 */
function setupProject() {
  var projectName = "My Internship Project"; // Change this
  
  // Create folders
  var folderIds = createProjectFolders(projectName);
  Logger.log("Created folders: " + JSON.stringify(folderIds));
  
  // Create KPI Dashboard
  var kpiSheet = createKPIDashboard(folderIds.reports, projectName);
  Logger.log("Created KPI Dashboard: " + kpiSheet.getUrl());
  
  // Create Content Calendar
  var contentSheet = createContentCalendar(folderIds.content, projectName);
  Logger.log("Created Content Calendar: " + contentSheet.getUrl());
  
  return {
    folders: folderIds,
    kpiDashboard: kpiSheet.getUrl(),
    contentCalendar: contentSheet.getUrl()
  };
}