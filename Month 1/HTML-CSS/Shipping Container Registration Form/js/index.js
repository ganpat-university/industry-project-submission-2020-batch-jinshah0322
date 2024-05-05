function areAllFieldsFilled(tabId) {
  var fields = document.querySelectorAll('#' + tabId + ' [required]');
  var allFilled = true;
  fields.forEach(function(field) {
      if (!field.value.trim()) {
          allFilled = false;
      }
  });
  return allFilled;
}

function navigateToTab(currentTab, nextTabId) {
  if (areAllFieldsFilled(currentTab)) {
      $('#' + nextTabId).tab('show');
  }
}

document.getElementById('nextToCaptain').addEventListener('click', function() {
  navigateToTab('ship-info', 'captain-tab');
});

document.getElementById('prevToShip').addEventListener('click', function() {
  $('#' + 'ship-tab').tab('show');
});

document.getElementById('nextToContainer').addEventListener('click', function() {
  navigateToTab('captain-info', 'container-tab');
});

document.getElementById('prevToCaptain').addEventListener('click', function() {
  $('#' + 'captain-tab').tab('show');
});

document.getElementById('nextToRoute').addEventListener('click', function() {
  navigateToTab('container-info', 'route-tab');
});

document.getElementById('prevToContainer').addEventListener('click', function() {
  $('#' + 'container-tab').tab('show');
});
