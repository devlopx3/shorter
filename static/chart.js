am4core.useTheme(am4themes_animated);

// Create chart instance
var chart = am4core.create("chartdiv", am4charts.PieChart);

chart.data = [{
    "country": "China",
    "name": 41
}, {
    "country": "United States",
    "name": 10
}, {
    "country": "Turkey",
    "name": 4.7
}, {
    "country": "Russia",
    "name": 4.3
}, {
    "country": "Taiwan",
    "name": 3.7
}, {
    "country": "Rest of the World",
    "name": 36.3
}];

// Add and configure Series
var pieSeries = chart.series.push(new am4charts.PieSeries());
pieSeries.dataFields.value = "name";
pieSeries.dataFields.category = "country";
pieSeries.innerRadius = am4core.percent(45);
pieSeries.ticks.template.disabled = true;
pieSeries.labels.template.disabled = true;

let rgm = new am4core.RadialGradientModifier();
rgm.brightnesses.push(-0.8, -0.8, -0.5, 0, - 0.5);
pieSeries.slices.template.fillModifier = rgm;
pieSeries.slices.template.strokeModifier = rgm;
pieSeries.slices.template.strokeOpacity = 0.4;
pieSeries.slices.template.strokeWidth = 0;

chart.legend = new am4charts.Legend();
chart.legend.position = "right";
var label = chart.createChild(am4core.Label);
label.text = "Top Hacking Crime Countries of Origin.";
label.fontSize = 32;
label.align = "center";
label.fontFamily = "impact";
