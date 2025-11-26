function barChart(elementId, title, data, xField, yField) {
    if (!data || data.length === 0) {
        document.getElementById(elementId).innerHTML = "<i>Nenhum dado ainda.</i>";
        return;
    }

    const trace = {
        x: data.map(d => d[xField]),
        y: data.map(d => d[yField]),
        type: 'bar'
    };

    const layout = {
        title: title,
        margin: { t: 40 }
    };

    Plotly.newPlot(elementId, [trace], layout);
}

barChart("portalChart", "Média por Portal", portalStats, "portal", "avg_placement");
barChart("compChart", "Média por Composição", compStats, "composition", "avg_placement");
barChart("augChart", "Média por Augment", augStats, "augment", "avg_placement");
