// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

// Pie Chart Example
var ctx = document.getElementById("winPieChartVP");
var winPieChartV = new Chart(ctx, {
  type: 'pie',
  data: {
    labels: ["Richard & Mortimer", "Gus & Oona", "Sam & Eleanor", "Dan & Anna", "Tim & Eric"],
    datasets: [{
      data: [25, 12, 15, 11, 8],
      backgroundColor: ['#007bff', '#dc3545', '#ffc107', '#28a745', '#7D3C98'],
    }],
  },
});

// Pie Chart Example
var ctx = document.getElementById("lossPieChartVP");
var lossPieChartV = new Chart(ctx, {
  type: 'pie',
  data: {
    labels: ["Glacier", "Flathead", "Skyview", "Butte", "Hellgate", "West", "Helena"],
    datasets: [{
      data: [20, 30, 10, 4, 5, 8, 10],
      backgroundColor: ['#007bff', '#dc3545', '#ffc107', '#28a745', "#7D3C98", "#545573", "#587573"],
    }],
  },
});

// Pie Chart Example
var ctx = document.getElementById("winPieChartN");
var winPieChartN = new Chart(ctx, {
  type: 'pie',
  data: {
    labels: ["Richard & Mortimer", "Gus & Oona", "Sam & Eleanor", "Dan & Anna", "Tim & Eric"],
    datasets: [{
      data: [10, 12, 30, 5, 8],
      backgroundColor: ['#007bff', '#dc3545', '#ffc107', '#28a745', "#545573"],
    }],
  },
});

// Pie Chart Example
var ctx = document.getElementById("lossPieChartN");
var lossPieChartN = new Chart(ctx, {
  type: 'pie',
  data: {
    labels: ["Glacier", "Flathead", "Skyview", "Butte", "Hellgate", "West", "Helena"],
    datasets: [{
      data: [20, 20, 10, 50, 5, 5, 10],
      backgroundColor: ['#007bff', '#dc3545', '#ffc107', '#28a745', "#7D3C98", "#545573", "#587573"],
    }],
  },
});
