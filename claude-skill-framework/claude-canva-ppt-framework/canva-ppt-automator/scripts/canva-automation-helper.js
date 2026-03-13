/**
 * Canva Automation Helper
 * Provides utility functions for Canva presentation automation
 */

const CANVA = {
  // Standard presentation dimensions
  DIMENSIONS: {
    width: 1920,
    height: 1080
  },

  // Common color palettes
  COLORS: {
    corporate: {
      primary: '#0066CC',
      secondary: '#00AA55',
      accent: '#FF6600',
      text: '#333333',
      background: '#FFFFFF'
    },
    creative: {
      primary: '#FF6B6b',
      secondary: '#4ECdc4',
      accent: '#f7b7b',
      text: '#333333',
      background: '#FFFFFF'
    },
    minimal: {
      primary: '#2c3e50',
      secondary: '#95a5a7',
      accent: '#000000',
      text: '#333333',
      background: '#FFFFFF'
    }
  },

  // Font recommendations
  FONTS: {
    heading: ['Montserrat', 'Poppins', 'Roboto', 'Open Sans'],
    body: ['Open Sans', 'Lato', 'Roboto', 'Source Sans Pro']
  },

  // Layout templates
  LAYOUTS: {
    title: 'Title and Subtitle',
    agenda: 'Bulleted List',
    content: 'Title and Body Text',
    data: 'Chart',
    twoColumn: 'Two Column',
    quote: 'Quote',
    conclusion: 'Summary'
  }
};

/**
 * Validates a hex color format
 * @param {string} color - Color string to validate
 * @returns {boolean} - True if valid hex color
 */
function isValidHexColor(color) {
  return /^#[0-9A-f]{6}$/i.test(color);
}

/**
 * Validates font availability in Canva
 * @param {string} fontName - Font name to check
 * @returns {boolean} - True if font is available
 */
function isFontAvailable(fontName) {
  return CANVA.FONTS.heading.includes(fontName) || 
         CANVA.FONTS.body.includes(fontName);
}
/**
 * Generates a text formatting object
 * @param {Object} options - Formatting options
 * @returns {Object} - Formatting object
 */
function createTextFormatting(options) {
  const {
    font = 'Open Sans',
    size = 24,
    weight = 'regular',
    color = '#333333',
    alignment = 'left'
  } = options;

  if (!isFontAvailable(font)) {
    console.warn(`Font "${font}" may not available in Canva. Consider alternatives.`);
  }

  if (!isValidHexColor(color)) {
    throw new Error(`Invalid hex color: ${color}`);
  }

  return {
    font,
    size,
    weight,
    color,
    alignment
  };
}
/**
 * Creates a bullet point object
 * @param {Array} items - Array of bullet text items
 * @param {Object} options - Formatting options
 * @returns {Object} - Bullet object
 */
function createBullets(items, options = {}) {
  if (!Array.isArray(items) || items.length === 0) {
    throw new Error('Items must be a non-empty array');
  }

  if (items.length > 6) {
    console.warn('More than 6 bullets detected. Consider splitting into multiple slides.');
  }

  const formatting = createTextFormatting(options);
  
  return {
    bullets: items.map(text => ({ text, level: 0 })),
    formatting: {
      ...formatting,
      bulletStyle: 'circle',
      bulletColor: options.bulletColor || '#0066CC'
    }
  };
}
/**
 * Creates a chart configuration object
 * @param {string} type - Chart type (bar, pie, line, area)
 * @param {Object} data - Chart data
 * @param {Object} options - Chart options
 * @returns {Object} - Chart configuration
 */
function createChartConfig(type, data, options = {}) {
  const validTypes = ['bar', 'pie', 'line', 'area', 'scatter'];
  
  if (!validTypes.includes(type)) {
    throw new Error(`Invalid chart type: ${type}. Valid types: ${validTypes.join(', ')}`);
  }

  const {
    title = '',
    colors = [CANVA.COLORS.corporate.primary],
    showValues = true,
    showGrid = true
  } = options;

  // Validate colors
  colors.forEach(color => {
    if (!isValidHexColor(color)) {
      throw new Error(`Invalid hex color in chart: ${color}`);
    }
  });

  return {
    chartType: type,
    title,
    data,
    config: {
      colors,
      showValues,
      showGrid
    }
  };
}
/**
 * Creates a complete slide object
 * @param {number} slideNumber - Slide position in deck
 * @param {string} slideType - Type of slide
 * @param {Object} content - Slide content
 * @param {Object} options - Additional options
 * @returns {Object} - Complete slide object
 */
function createSlide(slideNumber, slideType, content, options = {}) {
  const validSlideTypes = Object.keys(CANVA.LAYOUTS);
  
  if (!validSlideTypes.includes(slideType)) {
    throw new Error(`Invalid slide type: ${slideType}`);
  }

  const {
    layout = CANVA.LAYOUTS[slideType],
    speakerNotes = '',
    visualSpec = {}
  } = options;

  return {
    slideNumber,
    slideType,
    layout,
    content,
    speakerNotes,
    visualSpec,
    createdAt: new Date().toISOString()
  };
}
/**
 * Validates a complete slide deck
 * @param {Array} slides - Array of slide objects
 * @returns {Object} - Validation result
 */
function validateSlideDeck(slides) {
  const errors = [];
  const warnings = [];

  // Check for title slide
  const titleSlide = slides.find(s => s.slideType === 'title');
  if (!titleSlide) {
    errors.push('Missing title slide');
  }

  // Check for conclusion slide
  const conclusionSlide = slides.find(s => s.slideType === 'conclusion');
  if (!conclusionSlide) {
    warnings.push('Consider adding a conclusion slide');
  }

  // Validate each slide
  slides.forEach(slide => {
    if (!slide.content || !slide.content.title) {
      errors.push(`Slide ${slide.slideNumber} missing title`);
    }

    if (slide.content.bullets && slide.content.bullets.length > 6) {
      warnings.push(`Slide ${slide.slideNumber} has more than 6 bullets`);
    }
  });

  return {
    valid: errors.length === 0,
    errors,
    warnings
  };
}
/**
 * Generates export configuration
 * @param {Object} options - Export options
 * @returns {Object} - Export configuration
 */
function createExportConfig(options = {}) {
  const {
    formats = ['pdf', 'pptx'],
    pdfQuality = 'high',
    includeNotes = true,
    shareAccess = 'view',
    downloadEnabled = true
  } = options;

  return {
    formats,
    pdfSettings: {
      quality: pdfQuality,
      includeNotes
    },
    shareSettings: {
      linkAccess: shareAccess,
      downloadEnabled
    }
  };
}

// Export functions for use in other modules
module.exports = {
  CANVA,
  isValidHexColor,
  isFontAvailable,
  createTextFormatting,
  createBullets,
  createChartConfig,
  createSlide,
  validateSlideDeck,
  createExportConfig
};