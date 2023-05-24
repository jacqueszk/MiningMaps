function onDropdownChange(event) {
    var selectedCompany = event.target.value;
    filterByCompany(selectedCompany);
}

function filterByCompany(company) {
    for (var i = 0; i < markers.length; i++) {
        var marker = markers[i];
        var markerCompany = marker.getTooltip().getContent();
        if (company === 'all' || markerCompany === company) {
            marker.addTo(map);
        } else {
            marker.removeFrom(map);
        }
    }
}

var dropdown = document.getElementById('company-filter');
dropdown.addEventListener('change', onDropdownChange);

// Initial filtering based on the selected company
var selectedCompany = dropdown.value;
filterByCompany(selectedCompany);
