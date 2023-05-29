// Function to handle form submission
function handleFormSubmit(event) {
  event.preventDefault();

  // Get form field values
  var selectedClass = document.getElementById("class").value;
  // Retrieve other form field values as needed

  // Perform validation and submit data to backend or display success message
  // ...

  // Clear form fields after submission
  event.target.reset();
}

// Function to fetch and display class schedule
function fetchClassSchedule() {
  // Fetch class schedule data from backend API
  // ...

  // Assuming the response is an array of class objects
  var classSchedule = [
    { class: "Class 1", date: "2023-06-01", time: "10:00 AM", spotsAvailable: 5 },
    { class: "Class 2", date: "2023-06-02", time: "11:30 AM", spotsAvailable: 8 },
    // Add more class objects here
  ];

  // Display class schedule in the webpage
  var scheduleDiv = document.getElementById("schedule");
  scheduleDiv.innerHTML = "";
  for (var i = 0; i < classSchedule.length; i++) {
    var classObj = classSchedule[i];
    var scheduleItem = document.createElement("div");
    scheduleItem.innerHTML = "<strong>" + classObj.class + "</strong> - Date: " + classObj.date + ", Time: " + classObj.time + ", Spots Available: " + classObj.spotsAvailable;
    scheduleDiv.appendChild(scheduleItem);
  }
}

// Add event listener and execute necessary functions when the page loads
document.addEventListener("DOMContentLoaded", function() {
  // Fetch and display class schedule
  fetchClassSchedule();

  // Add event listener for form submission
  var bookingForm = document.getElementById("booking-form");
  bookingForm.addEventListener("submit", handleFormSubmit);
});
