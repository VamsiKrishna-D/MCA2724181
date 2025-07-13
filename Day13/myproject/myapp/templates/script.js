var selectedRow = null;
function onFormSubmit() {
var formData = readFormData();
if(isValid()){
    if (selectedRow == null) {
    insertNewRecord(formData);
    alert("Your details are saved Sucessfully........");
  }
 else{
  updateRecord(formData);
 }
  resetForm();
}
}

function readFormData() {
  var formData = {};
  formData["facName"] = document.getElementById("facName").value;
  formData["facDep"] = document.getElementById("facDep").value;
  formData["facSub"] = document.getElementById("facSub").value;
  formData["facAge"] = document.getElementById("facAge").value;
  formData["facPlace"] = document.getElementById("facPlace").value;
  return formData;
}
function resetForm() {
  document.getElementById("facName").value = "";
  document.getElementById("facDep").value = "";
  document.getElementById("facSub").value = "";
  document.getElementById("facAge").value = "";
  document.getElementById("facPlace").value = "";
  selectedRow = null;
}
function insertNewRecord(data) {
  var table = document
    .getElementById("faclist")
    .getElementsByTagName("tbody")[0];
  var newRow = table.insertRow(table.length);
  cell1 = newRow.insertCell(0);
  cell1.innerHTML = data.facName;
  cell2 = newRow.insertCell(1);
  cell2.innerHTML = data.facDep;
  cell3 = newRow.insertCell(2);
  cell3.innerHTML = data.facSub;
  cell4 = newRow.insertCell(3);
  cell4.innerHTML = data.facAge;
  cell5 = newRow.insertCell(4);
  cell5.innerHTML = data.facPlace;
  cell6 = newRow.insertCell(5);
  cell6.innerHTML = `<a onClick="onEdit(this)">Update</a><a onClick="onDelete(this)">Delete</a>`;
}
function onEdit(td)
{if(confirm("Are you upadate your details")){
selectedRow=td.parentElement.parentElement;  
document.getElementById("facName").value=selectedRow.cells[0].innerHTML;
document.getElementById("facDep").value=selectedRow.cells[1].innerHTML;
document.getElementById("facSub").value=selectedRow.cells[2].innerHTML;
document.getElementById("facAge").value=selectedRow.cells[3].innerHTML;
document.getElementById("facPlace").value=selectedRow.cells[4].innerHTML;}
}
function updateRecord(formData)
{
  alert("Your form updated sucessfully.......")
selectedRow.cells[0].innerHTML=formData.facName;
selectedRow.cells[1].innerHTML=formData.facDep;
selectedRow.cells[2].innerHTML=formData.facSub;
selectedRow.cells[3].innerHTML=formData.facAge;
selectedRow.cells[4].innerHTML=formData.facPlace;
}
function onDelete(td)
{
if(confirm("are you want to delete this record")){
  row=td.parentElement.parentElement;
  document.getElementById("faclist").deleteRow(row.rowIndex);
  resetForm();
}
}

/*function isValid(){
var a=document.getElementById("facName").value;
// var b = document.getElementById("facDep").value;
// var c= document.getElementById("facSub").value;
// var d= document.getElementById("facAge").value;
// var e= document.getElementById("facPlace").value;
if(a==""|| a==null ){return false;}
else
{return true;}

}*/
function isValid(){
var a=document.getElementById("facName").value;
if(a==""|| a==null )
  {alert("please enter name");return false;}
 var  b = document.getElementById("facDep").value;
if(b==""|| b==null ){alert("please enter department");return false;}
 var c= document.getElementById("facSub").value;
if(c==""|| c==null ){alert("please enter sub");return false;}
 var d= document.getElementById("facAge").value;
if(d<18|| d>60 ){alert("please enter age");return false;}
  var e= document.getElementById("facPlace").value;
if(e==""|| e==null ){alert("please enter place");return false;}
else
{return true;}

}
 
  









/*const agePattern = /^(?:[2-3][0-9]?|30)$/;
if (!agePattern.test(ageStr)) {
  ageError.textContent = 'Enter a valid age between 1 and 100.';
  return false;
}
function onFormSubmit() {
  const ageInput = document.getElementById('facAge');
  const age = parseInt(ageInput.value, 10);

  if (isNaN(age) || age < 18 || age > 100) {
    alert("Please enter a valid age between 18 and 100.");
    ageInput.focus();
    return false;
  }

  // Proceed with form submission or other logic
  // For example, you can call a function to add the data to the table
  // addFacultyDetails();
}
const ageStr = ageInput.value.trim();
const agePattern = /^[1-9]?\d$|^100$/;  // matches 1‑99, 100
if (!agePattern.test(ageStr)) {
  alert("⚠️ Age must be between 1 and 100.");
  ageInput.focus();
  return false;
}<div>
  <label for="facAge">Age</label><br />
  <input
    type="number"
    class="facAge"
    id="facAge"
    placeholder="Enter age"
  />
  <div id="facAgeError" style="color:red; font-size:0.9em;"></div>
</div>
function onFormSubmit() {
  const ageInput = document.getElementById("facAge");
  const ageError = document.getElementById("facAgeError");
  const ageValue = ageInput.value.trim();

  ageError.textContent = ""; // clear previous error

  // Check if age is empty
  if (ageValue === "") {
    ageError.textContent = "Age is required.";
    return;
  }

  const age = parseInt(ageValue, 10);
  if (isNaN(age) || age < 18 || age > 100) {
    ageError.textContent = "Age must be a number between 18 and 100.";
    return;
  }

  // If valid: proceed to add faculty record
  appendToFacultyList();  // your existing append logic
}
<form onsubmit="event.preventDefault(); onFormSubmit();">
  <!-- other fields... -->
  <!-- updated age field with error span -->
  <div>…</div>
  <div><input type="submit" value="Submit" /></div>
</form>
*/
