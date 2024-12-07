// Configuration for Looker Studio dashboards
const dashboards = {
  dashboard1: {
    embedUrl: 'https://lookerstudio.google.com/embed/reporting/a12b260a-7227-490b-a9bf-48911528b67b/page/nbMYE',
  },
  dashboard2: {
    embedUrl: 'https://lookerstudio.google.com/embed/reporting/5718d46b-04fc-4bdf-a3ca-69ce70377378/page/TvMYE',
  },
  dashboard3: {
    embedUrl: 'https://lookerstudio.google.com/embed/reporting/d0d0d6a9-2abb-4254-9fbe-239818320fa9/page/EGNYE',
  },
  
};

// Embed container element
const iframe = document.getElementById('dashboardIframe');

// Function to load a Looker Studio dashboard
function loadDashboard(dashboardKey) {
  const dashboardConfig = dashboards[dashboardKey];
  
  // Update iframe source to load the selected dashboard
  iframe.src = dashboardConfig.embedUrl;
}

// Load the first dashboard by default
loadDashboard('dashboard1');
