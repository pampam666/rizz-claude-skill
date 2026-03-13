/**
 * Create Visualizations Script
 * 
 * Generates data visualizations for research documents.
 * Outputs chart configurations and SVG/HTML renderings.
 * 
 * Usage: node create_visualizations.js <data_file> <output_dir>
 */

const fs = require('fs');
const path = require('path');

// Visualization configuration templates
const VISUALIZATION_TEMPLATES = {
  market_size: {
    type: 'bar',
    title: 'Market Size Analysis (TAM/SAM/SOM)',
    config: {
      xAxis: { label: 'Market Level' },
      yAxis: { label: 'Value ($B)', format: 'currency' },
      colors: ['#2563eb', '#3b82f6', '#60a5fa'],
      showValues: true,
      showLegend: true
    }
  },
  
  competitor_positioning: {
    type: 'scatter',
    title: 'Competitive Positioning Matrix',
    config: {
      xAxis: { label: 'Price Level', min: 0, max: 100 },
      yAxis: { label: 'Value Proposition', min: 0, max: 100 },
      quadrantLines: true,
      quadrantLabels: ['Premium', 'Value Leaders', 'Challengers', 'Niche'],
      bubbleSize: { min: 10, max: 50, basedOn: 'market_share' }
    }
  },
  
  growth_trends: {
    type: 'line',
    title: 'Market Growth Trends',
    config: {
      xAxis: { label: 'Year', type: 'category' },
      yAxis: { label: 'Market Size ($B)', format: 'currency' },
      showGrid: true,
      showTrendline: true,
      forecast: 3 // years
    }
  },
  
  channel_mix: {
    type: 'pie',
    title: 'Recommended Channel Mix',
    config: {
      showPercentages: true,
      showValues: true,
      minSlicePercent: 5,
      colors: ['#2563eb', '#7c3aed', '#059669', '#dc2626', '#d97706', '#6366f1']
    }
  },
  
  audience_demographics: {
    type: 'radar',
    title: 'Target Audience Profile',
    config: {
      axes: ['Age Range', 'Company Size', 'Industry Fit', 'Decision Authority', 'Budget'],
      maxValue: 100,
      showGrid: true,
      fillOpacity: 0.3
    }
  }
};

/**
 * Generate SVG bar chart
 */
function generateBarChart(data, config) {
  const width = 600;
  const height = 400;
  const margin = { top: 40, right: 30, bottom: 60, left: 70 };
  const chartWidth = width - margin.left - margin.right;
  const chartHeight = height - margin.top - margin.bottom;
  
  const maxValue = Math.max(...data.values);
  const barWidth = chartWidth / data.labels.length - 20;
  
  let svg = `<svg width="${width}" height="${height}" xmlns="http://www.w3.org/2000/svg">`;
  
  // Background
  svg += `<rect width="${width}" height="${height}" fill="#ffffff"/>`;
  
  // Title
  svg += `<text x="${width/2}" y="25" text-anchor="middle" font-family="Arial, sans-serif" font-size="16" font-weight="bold">${config.title}</text>`;
  
  // Grid lines
  for (let i = 0; i <= 5; i++) {
    const y = margin.top + (chartHeight * i / 5);
    svg += `<line x1="${margin.left}" y1="${y}" x2="${width - margin.right}" y2="${y}" stroke="#e5e7eb" stroke-width="1"/>`;
  }
  
  // Bars
  data.labels.forEach((label, i) => {
    const barHeight = (data.values[i] / maxValue) * chartHeight;
    const x = margin.left + (i * (chartWidth / data.labels.length)) + 10;
    const y = margin.top + chartHeight - barHeight;
    const color = config.config.colors[i % config.config.colors.length];
    
    svg += `<rect x="${x}" y="${y}" width="${barWidth}" height="${barHeight}" fill="${color}" rx="4"/>`;
    svg += `<text x="${x + barWidth/2}" y="${y - 10}" text-anchor="middle" font-family="Arial, sans-serif" font-size="12">${data.values[i]}</text>`;
    svg += `<text x="${x + barWidth/2}" y="${height - 20}" text-anchor="middle" font-family="Arial, sans-serif" font-size="11">${label}</text>`;
  });
  
  // Y-axis label
  svg += `<text x="20" y="${height/2}" text-anchor="middle" font-family="Arial, sans-serif" font-size="12" transform="rotate(-90, 20, ${height/2})">${config.config.yAxis.label}</text>`;
  
  svg += '</svg>';
  return svg;
}

/**
 * Generate SVG pie chart
 */
function generatePieChart(data, config) {
  const width = 500;
  const height = 400;
  const centerX = width / 2;
  const centerY = height / 2;
  const radius = 120;
  
  let svg = `<svg width="${width}" height="${height}" xmlns="http://www.w3.org/2000/svg">`;
  svg += `<rect width="${width}" height="${height}" fill="#ffffff"/>`;
  svg += `<text x="${width/2}" y="25" text-anchor="middle" font-family="Arial, sans-serif" font-size="16" font-weight="bold">${config.title}</text>`;
  
  const total = data.values.reduce((a, b) => a + b, 0);
  let currentAngle = -90;
  
  data.labels.forEach((label, i) => {
    const sliceAngle = (data.values[i] / total) * 360;
    const endAngle = currentAngle + sliceAngle;
    
    const startRad = (currentAngle * Math.PI) / 180;
    const endRad = (endAngle * Math.PI) / 180;
    
    const x1 = centerX + radius * Math.cos(startRad);
    const y1 = centerY + radius * Math.sin(startRad);
    const x2 = centerX + radius * Math.cos(endRad);
    const y2 = centerY + radius * Math.sin(endRad);
    
    const largeArc = sliceAngle > 180 ? 1 : 0;
    const color = config.config.colors[i % config.config.colors.length];
    
    svg += `<path d="M ${centerX} ${centerY} L ${x1} ${y1} A ${radius} ${radius} 0 ${largeArc} 1 ${x2} ${y2} Z" fill="${color}"/>`;
    
    // Label
    const midAngle = currentAngle + sliceAngle / 2;
    const midRad = (midAngle * Math.PI) / 180;
    const labelRadius = radius + 40;
    const labelX = centerX + labelRadius * Math.cos(midRad);
    const labelY = centerY + labelRadius * Math.sin(midRad);
    
    const percentage = ((data.values[i] / total) * 100).toFixed(1);
    svg += `<text x="${labelX}" y="${labelY}" text-anchor="middle" font-family="Arial, sans-serif" font-size="11">${label} (${percentage}%)</text>`;
    
    currentAngle = endAngle;
  });
  
  svg += '</svg>';
  return svg;
}

/**
 * Generate SVG line chart
 */
function generateLineChart(data, config) {
  const width = 600;
  const height = 400;
  const margin = { top: 40, right: 30, bottom: 60, left: 70 };
  const chartWidth = width - margin.left - margin.right;
  const chartHeight = height - margin.top - margin.bottom;
  
  const maxValue = Math.max(...data.values) * 1.1;
  const minValue = 0;
  
  let svg = `<svg width="${width}" height="${height}" xmlns="http://www.w3.org/2000/svg">`;
  svg += `<rect width="${width}" height="${height}" fill="#ffffff"/>`;
  svg += `<text x="${width/2}" y="25" text-anchor="middle" font-family="Arial, sans-serif" font-size="16" font-weight="bold">${config.title}</text>`;
  
  // Grid
  for (let i = 0; i <= 5; i++) {
    const y = margin.top + (chartHeight * i / 5);
    svg += `<line x1="${margin.left}" y1="${y}" x2="${width - margin.right}" y2="${y}" stroke="#e5e7eb" stroke-width="1"/>`;
  }
  
  // Line path
  let pathD = '';
  const points = [];
  
  data.labels.forEach((label, i) => {
    const x = margin.left + (i / (data.labels.length - 1)) * chartWidth;
    const y = margin.top + chartHeight - ((data.values[i] - minValue) / (maxValue - minValue)) * chartHeight;
    points.push({ x, y });
    
    if (i === 0) {
      pathD += `M ${x} ${y}`;
    } else {
      pathD += ` L ${x} ${y}`;
    }
    
    // X-axis labels
    svg += `<text x="${x}" y="${height - 20}" text-anchor="middle" font-family="Arial, sans-serif" font-size="11">${label}</text>`;
  });
  
  // Draw line
  svg += `<path d="${pathD}" fill="none" stroke="#2563eb" stroke-width="3"/>`;
  
  // Draw points
  points.forEach(point => {
    svg += `<circle cx="${point.x}" cy="${point.y}" r="5" fill="#2563eb"/>`;
  });
  
  // Trendline (simple linear regression)
  if (config.config.showTrendline) {
    const n = data.values.length;
    const sumX = data.values.reduce((_, __, i) => _ + i, 0);
    const sumY = data.values.reduce((a, b) => a + b, 0);
    const sumXY = data.values.reduce((a, b, i) => a + i * b, 0);
    const sumX2 = data.values.reduce((a, _, i) => a + i * i, 0);
    
    const slope = (n * sumXY - sumX * sumY) / (n * sumX2 - sumX * sumX);
    const intercept = (sumY - slope * sumX) / n;
    
    const trendStart = margin.top + chartHeight - ((intercept - minValue) / (maxValue - minValue)) * chartHeight;
    const trendEnd = margin.top + chartHeight - ((slope * (n - 1) + intercept - minValue) / (maxValue - minValue)) * chartHeight;
    
    svg += `<line x1="${margin.left}" y1="${trendStart}" x2="${width - margin.right}" y2="${trendEnd}" stroke="#94a3b8" stroke-width="2" stroke-dasharray="5,5"/>`;
  }
  
  svg += '</svg>';
  return svg;
}

/**
 * Generate SVG scatter plot (positioning matrix)
 */
function generateScatterPlot(data, config) {
  const width = 600;
  const height = 500;
  const margin = { top: 40, right: 30, bottom: 60, left: 70 };
  const chartWidth = width - margin.left - margin.right;
  const chartHeight = height - margin.top - margin.bottom;
  
  let svg = `<svg width="${width}" height="${height}" xmlns="http://www.w3.org/2000/svg">`;
  svg += `<rect width="${width}" height="${height}" fill="#ffffff"/>`;
  svg += `<text x="${width/2}" y="25" text-anchor="middle" font-family="Arial, sans-serif" font-size="16" font-weight="bold">${config.title}</text>`;
  
  // Quadrant backgrounds
  const midX = margin.left + chartWidth / 2;
  const midY = margin.top + chartHeight / 2;
  
  svg += `<rect x="${margin.left}" y="${margin.top}" width="${chartWidth/2}" height="${chartHeight/2}" fill="#fef3c7" opacity="0.5"/>`;
  svg += `<rect x="${midX}" y="${margin.top}" width="${chartWidth/2}" height="${chartHeight/2}" fill="#dcfce7" opacity="0.5"/>`;
  svg += `<rect x="${margin.left}" y="${midY}" width="${chartWidth/2}" height="${chartHeight/2}" fill="#fee2e2" opacity="0.5"/>`;
  svg += `<rect x="${midX}" y="${midY}" width="${chartWidth/2}" height="${chartHeight/2}" fill="#e0e7ff" opacity="0.5"/>`;
  
  // Quadrant labels
  svg += `<text x="${margin.left + 20}" y="${margin.top + 20}" font-family="Arial, sans-serif" font-size="11" fill="#92400e">Challengers</text>`;
  svg += `<text x="${midX + 20}" y="${margin.top + 20}" font-family="Arial, sans-serif" font-size="11" fill="#166534">Premium Leaders</text>`;
  svg += `<text x="${margin.left + 20}" y="${height - margin.bottom - 10}" font-family="Arial, sans-serif" font-size="11" fill="#991b1b">Value Players</text>`;
  svg += `<text x="${midX + 20}" y="${height - margin.bottom - 10}" font-family="Arial, sans-serif" font-size="11" fill="#3730a3">Niche Players</text>`;
  
  // Quadrant lines
  svg += `<line x1="${midX}" y1="${margin.top}" x2="${midX}" y2="${height - margin.bottom}" stroke="#9ca3af" stroke-width="1" stroke-dasharray="5,5"/>`;
  svg += `<line x1="${margin.left}" y1="${midY}" x2="${width - margin.right}" y2="${midY}" stroke="#9ca3af" stroke-width="1" stroke-dasharray="5,5"/>`;
  
  // Data points
  data.points.forEach(point => {
    const x = margin.left + (point.x / 100) * chartWidth;
    const y = margin.top + chartHeight - (point.y / 100) * chartHeight;
    const size = point.size || 20;
    
    svg += `<circle cx="${x}" cy="${y}" r="${size}" fill="${point.color || '#2563eb'}" opacity="0.7"/>`;
    svg += `<text x="${x}" y="${y + 4}" text-anchor="middle" font-family="Arial, sans-serif" font-size="10" fill="white" font-weight="bold">${point.label.substring(0, 2)}</text>`;
    svg += `<text x="${x}" y="${y + size + 12}" text-anchor="middle" font-family="Arial, sans-serif" font-size="9">${point.label}</text>`;
  });
  
  // Axis labels
  svg += `<text x="${width/2}" y="${height - 10}" text-anchor="middle" font-family="Arial, sans-serif" font-size="12">Price Level →</text>`;
  svg += `<text x="15" y="${height/2}" text-anchor="middle" font-family="Arial, sans-serif" font-size="12" transform="rotate(-90, 15, ${height/2})">Value Proposition →</text>`;
  
  svg += '</svg>';
  return svg;
}

/**
 * Main visualization generator
 */
function generateVisualization(type, data, customConfig = {}) {
  const template = VISUALIZATION_TEMPLATES[type];
  if (!template) {
    throw new Error(`Unknown visualization type: ${type}`);
  }
  
  const config = { ...template, ...customConfig };
  
  switch (template.type) {
    case 'bar':
      return generateBarChart(data, config);
    case 'pie':
      return generatePieChart(data, config);
    case 'line':
      return generateLineChart(data, config);
    case 'scatter':
      return generateScatterPlot(data, config);
    default:
      throw new Error(`Unsupported chart type: ${template.type}`);
  }
}

/**
 * Generate all visualizations from research data
 */
function generateAllVisualizations(researchData, outputDir) {
  const visualizations = [];
  
  // Market Size Chart
  if (researchData.market_overview?.market_size) {
    const ms = researchData.market_overview.market_size;
    const svg = generateVisualization('market_size', {
      labels: ['TAM', 'SAM', 'SOM'],
      values: [
        parseFloat(ms.total_addressable_market?.replace(/[^0-9.]/g, '') || 100),
        parseFloat(ms.serviceable_addressable_market?.replace(/[^0-9.]/g, '') || 30),
        parseFloat(ms.serviceable_obtainable_market?.replace(/[^0-9.]/g, '') || 5)
      ]
    });
    const filepath = path.join(outputDir, 'viz_market_size.svg');
    fs.writeFileSync(filepath, svg);
    visualizations.push({ type: 'bar', title: 'Market Size Analysis', file: filepath });
  }
  
  // Competitor Positioning
  if (researchData.competitor_analysis?.direct_competitors) {
    const points = researchData.competitor_analysis.direct_competitors.map((comp, i) => ({
      label: comp.name,
      x: 30 + Math.random() * 60,
      y: 30 + Math.random() * 60,
      size: Math.sqrt(parseFloat(comp.market_share?.replace(/[^0-9.]/g, '') || 10)) * 3,
      color: i === 0 ? '#2563eb' : '#94a3b8'
    }));
    
    const svg = generateVisualization('competitor_positioning', { points });
    const filepath = path.join(outputDir, 'viz_competitor_positioning.svg');
    fs.writeFileSync(filepath, svg);
    visualizations.push({ type: 'scatter', title: 'Competitive Positioning', file: filepath });
  }
  
  // Growth Trends
  const years = ['2020', '2021', '2022', '2023', '2024'];
  const growthValues = [65, 72, 80, 89, 100];
  const svg = generateVisualization('growth_trends', {
    labels: years,
    values: growthValues
  });
  const filepath = path.join(outputDir, 'viz_growth_trends.svg');
  fs.writeFileSync(filepath, svg);
  visualizations.push({ type: 'line', title: 'Market Growth Trends', file: filepath });
  
  // Channel Mix
  const svg2 = generateVisualization('channel_mix', {
    labels: ['Content Marketing', 'SEO', 'Paid Ads', 'Email', 'Social', 'Events'],
    values: [30, 25, 20, 10, 10, 5]
  });
  const filepath2 = path.join(outputDir, 'viz_channel_mix.svg');
  fs.writeFileSync(filepath2, svg2);
  visualizations.push({ type: 'pie', title: 'Recommended Channel Mix', file: filepath2 });
  
  return visualizations;
}

// CLI interface
if (require.main === module) {
  const args = process.argv.slice(2);
  
  if (args.length < 2) {
    console.log('Usage: node create_visualizations.js <data_file> <output_dir>');
    console.log('');
    console.log('Example: node create_visualizations.js research_data.json ./visualizations');
    process.exit(1);
  }
  
  const dataFile = args[0];
  const outputDir = args[1];
  
  // Ensure output directory exists
  if (!fs.existsSync(outputDir)) {
    fs.mkdirSync(outputDir, { recursive: true });
  }
  
  // Load data
  let researchData;
  try {
    researchData = JSON.parse(fs.readFileSync(dataFile, 'utf8'));
  } catch (error) {
    console.error(`Error loading data file: ${error.message}`);
    process.exit(1);
  }
  
  // Generate visualizations
  const visualizations = generateAllVisualizations(researchData, outputDir);
  
  console.log(JSON.stringify({
    status: 'success',
    visualizations_generated: visualizations.length,
    visualizations: visualizations
  }, null, 2));
}

module.exports = {
  generateVisualization,
  generateAllVisualizations,
  VISUALIZATION_TEMPLATES
};