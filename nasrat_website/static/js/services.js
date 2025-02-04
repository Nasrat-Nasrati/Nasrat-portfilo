// services.js
function openPopup(name, description) {
  document.getElementById('popupTitle').innerText = name;
  document.getElementById('popupDescription').innerText = description;
  document.getElementById('servicePopup').style.display = 'flex';
}

function closePopup() {
  document.getElementById('servicePopup').style.display = 'none';
}

// Close the popup if the user clicks outside of it
window.onclick = function(event) {
  var popup = document.getElementById('servicePopup');
  if (event.target == popup) {
    closePopup();
  }
};
