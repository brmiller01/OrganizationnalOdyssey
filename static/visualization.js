function fetchAndCreateChart() {
    fetch('/visualize')
        .then(response => response.json())
        .then(data => {
            anychart.onDocumentReady(function () {
                // create a chart and set the data
                var chart = anychart.graph({
                    nodes: data.nodes,
                    edges: data.links.map(link => ({
                        from: link.from,
                        to: link.to,
                        labels: [{text: link.label, enabled: true}]
                    }))
                });

                chart.nodes().labels().enabled(true);
                chart.nodes().labels().format("{%name}");
                chart.nodes().labels().fontSize(12);
                chart.nodes().labels().fontWeight(600);

                chart.edges().arrows().enabled(true);
                chart.tooltip().useHtml(true);

                // set the container id
                chart.container("chart_container");

                // initiate drawing the chart
                chart.draw();
            });
        });
}

document.addEventListener("DOMContentLoaded", function () {
    fetchAndCreateChart();
});
