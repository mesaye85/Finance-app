from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    html = '''<html>
  <head>
    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <title></title>
    <meta name="description" content="" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <link rel="preconnect" href="https://fonts.gstatic.com" />
    <link
      href="https://fonts.googleapis.com/css2?family=Rajdhani:wght@300&display=swap"
      rel="stylesheet"
    />
    <link rel="stylesheet" href="style.css" />
  </head>
  <body>
    <header>
      <div class="topnav">
        <h1 class="logo"><a href="#">FinanceApp</a></h1>

        <input type="text" placeholder="Search.." />
      </div>
    </header>
    <main>
      <div class="chart">
        <div id="donutchart" style="width: 900px; height: 500px"></div>
      </div>
      <div class="opc">
        <a href="login.html"
          ><button type="button"><h3>Plan For Retirement</h3></button></a
        >
        <a href="login.html"
          ><button type="button"><h3>Plan For A Big Purchase</h3></button></a
        >
        <a href="login.html"
          ><button type="button"><h3>Track Your Spending</h3></button></a
        >
      </div>
      <button type="button" class="btn btn-primary btn-lg">Login</button>
      <button type="button" class="btn btn-secondary btn-lg">
        Sign Up
      </button>
    </main>

    <footer>
      <a href="#"><h4>Personal Finance App</h4></a>
      <h3>Services</h3>
      <ul>
        <li>
          <a href=""><p>Retirement Planning</p></a>
        </li>
        <li>
          <a href=""><p>Plan For Purchase</p></a>
        </li>
        <li>
          <a href=""><p>Plan Your Budget</p></a>
        </li>
      </ul>
    </footer>
    <script
      type="text/javascript"
      src="https://www.gstatic.com/charts/loader.js"
    ></script>
    <script type="text/javascript">
      google.charts.load("current", { packages: ["corechart"] });
      google.charts.setOnLoadCallback(drawChart);
      function drawChart() {
        var data = google.visualization.arrayToDataTable([
          ["Task", "Hours per Day"],
          ["Rent/Mortgage", 11],
          ["Utilities", 2],
          ["Commute", 2],
          ["Entertainment", 2],
          ["Misc", 7],
        ]);

        var options = {
          title: "My Daily Spending",
          pieHole: 0.4,
        };

        var chart = new google.visualization.PieChart(
          document.getElementById("donutchart")
        );
        chart.draw(data, options);
      }
    </script>
    <script src="" async defer></script>
  </body>
</html>'''
    return HttpResponse(html)

