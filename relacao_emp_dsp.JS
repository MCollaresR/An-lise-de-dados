google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawVisualization);

function drawVisualization() {
    // Some raw data (not necessarily accurate)
    var data = google.visualization.arrayToDataTable([
        ['Ano de Abertura/ Fechamento', 'Abertura', 'Fechamento', 'Diferença Abertura/ Fechamento'],
        ['2014',  27995,   4825,  23170],
        ['2015',  28988,   6626,  22362],
        ['2016',  28011,   10224, 17787],
        ['2017',  29622,   8168,  21454],
        ['2018 - 100% digital',  30952,   31244,  -292],
        ['2019',  37908,   12751, 25157],
        ['2020',  44320,   12145, 32175],
        ['2021',  52269,   15635, 36634],
    ]);

    var options = {
        title : 'Tendência de Abertura/ Fechamento de empresas no Maranhão',
        vAxis: {title: 'Qauntidade de Empresas'},
        hAxis: {title: 'Ano de Abertura/ Fechamento'},
        seriesType: 'bars',
        series: {2: {type: 'line'}}
    };

    var chart = new google.visualization.ComboChart(document.getElementById('chart_div'));
    chart.draw(data, options);
    }