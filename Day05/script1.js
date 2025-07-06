
let selectedRow = null;
 function onFormSubmit()
  { 
   const formData = readFormData();
    if (isValid(formData)) { if (selectedRow === null) { insertNewRecord(formData); alert("Your details are saved successfully."); } else { updateRecord(formData); } resetForm(); } else { alert("Please fill in all fields."); } } function readFormData() { return { facName: document.getElementById("facName").value.trim(), facDep: document.getElementById("facDep").value.trim(), facSub: document.getElementById("facSub").value.trim() }; } function insertNewRecord(data) { const table = document.getElementById("faclist").getElementsByTagName("tbody")[0]; const newRow = table.insertRow(); newRow.insertCell(0).innerHTML = data.facName; newRow.insertCell(1).innerHTML = data.facDep; newRow.insertCell(2).innerHTML = data.facSub; newRow.insertCell(3).innerHTML = ` <a href="#" onClick="onEdit(this)">Update</a> | <a href="#" onClick=...



