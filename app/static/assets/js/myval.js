
function myfun(){
    var d = [
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 0, 6, 7, 8, 9, 5], 
        [2, 3, 4, 0, 1, 7, 8, 9, 5, 6], 
        [3, 4, 0, 1, 2, 8, 9, 5, 6, 7], 
        [4, 0, 1, 2, 3, 9, 5, 6, 7, 8], 
        [5, 9, 8, 7, 6, 0, 4, 3, 2, 1], 
        [6, 5, 9, 8, 7, 1, 0, 4, 3, 2], 
        [7, 6, 5, 9, 8, 2, 1, 0, 4, 3], 
        [8, 7, 6, 5, 9, 3, 2, 1, 0, 4], 
        [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
      ]
      var p = [
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 
        [1, 5, 7, 6, 2, 8, 3, 0, 9, 4], 
        [5, 8, 0, 3, 7, 9, 6, 1, 4, 2], 
        [8, 9, 1, 6, 0, 4, 3, 5, 2, 7], 
        [9, 4, 5, 3, 1, 2, 6, 8, 7, 0], 
        [4, 2, 8, 6, 5, 7, 3, 9, 0, 1], 
        [2, 7, 9, 3, 8, 0, 6, 4, 1, 5], 
        [7, 0, 4, 6, 9, 1, 3, 2, 5, 8]
      ]
    var a = document.getElementById("mobile").value;
    var b = document.getElementById("mobile_alt").value;
    var aadharno =  document.getElementById("aadhar").value;
    var name = document.getElementById("name").value;
    var company = document.getElementById("company").value;
    var occupation = document.getElementById("occupation").value;
    var residential = document.getElementById("residential").value;
    var corresponding = document.getElementById("corresponding").value;
    var email = document.getElementById("email").value;
    var invest = document.getElementById("invest").value;
    const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    
    if(name==""){

        notie.alert({ type: 'warning',position: 'bottom',text: 'Please enter your name!' })
        document.getElementById("name").focus();
         return false;
    }
    if(company==""){

        notie.alert({ type: 'warning',position: 'bottom',text: 'Please enter your company name!' })
        document.getElementById("company").focus();
         return false;
    }
    if(occupation==""){

        notie.alert({ type: 'warning',position: 'bottom',text: 'Please enter your occupation!' })
        document.getElementById("company").focus();
         return false;
    }
    
    if(residential==""){

        notie.alert({ type: 'warning',position: 'bottom',text: 'Please enter your residential address!' })
        document.getElementById("residential").focus();
         return false;
    }

    if(email==""){

        notie.alert({ type: 'warning',position: 'bottom',text: 'Please enter your email address!' })
        document.getElementById("email").focus();
         return false;
    }

    if(!(re.test(email))){
        notie.alert({ type: 'warning',position: 'bottom',text: 'Please enter correct email address!' })
        document.getElementById("email").focus();
         return false;
    }

    if(invest==""){

        notie.alert({ type: 'warning',position: 'bottom',text: 'Please enter investment amount' })
        document.getElementById("invest").focus();
         return false;
    }

    if(isNaN(invest)){

        notie.alert({ type: 'warning',position: 'bottom',text: 'Please enter valid amount' })
        document.getElementById("invest").focus();
         return false;
    }



    
   
    if (isNaN(a)){
        document.getElementById("mobile").value="";
        notie.alert({ type: 'warning',position: 'bottom',text: 'Please enter correct mobile number!' })
        document.getElementById("mobile").focus();
         return false;
    }
    if(a.length<10){
        document.getElementById("mobile").value="";
        notie.alert({ type: 'warning',position: 'bottom',text: 'Mobile Number can not be less than 10 digits' })
          document.getElementById("mobile").focus();
         return false;
    }
    if(a.length>10){
        document.getElementById("mobile").value="";
        notie.alert({ type: 'warning',position: 'bottom',text: 'Mobile Number can not be more than 10 digits' })
        document.getElementById("mobile").focus();
         return false;
    }
    if (isNaN(b)){
        document.getElementById("mobile_alt").value="";
        notie.alert({ type: 'warning',position: 'bottom',text: 'The number you entered is not valid!' })
        document.getElementById("mobile_alt").focus();
        return false;
    }
    if(b.length<10){
        document.getElementById("mobile_alt").value="";
        notie.alert({ type: 'warning',position: 'bottom',text: 'Please enter a valid phone number!' })
        document.getElementById("mobile_alt").focus();
        return false;
    }
    if(b.length>10){
        document.getElementById("mobile_alt").value="";
        notie.alert({ type: 'warning',position: 'bottom',text: 'Mobile Number can not be more than 10 digits' })
        document.getElementById("mobile_alt").focus();
        return false;
    }
    if(document.getElementById("mobile").value == document.getElementById("mobile_alt").value){
        document.getElementById("mobile_alt").value="";
        notie.alert({ type: 'warning',position: 'bottom',text: 'Please enter the alternative Mobile Number!' })
        document.getElementById("mobile_alt").focus();
        return false;
    }
    if(isNaN(aadharno))
    {
        document.getElementById("aadhar").value="";
        notie.alert({ type: 'warning',position: 'bottom',text: 'Aadhar Number can contain numbers only!' })
        document.getElementById("aadhar").focus();
         return false;
    }
   

   
    if(aadharno.length!=12)
    {   document.getElementById("aadhar").value="";
        notie.alert({ type: 'warning',position: 'bottom',text: 'Aadhar Number can contain 12 digits only!' })
        document.getElementById("aadhar").focus();
        return false;
    }
    
   
   
   
   
      var c = 0;
      var invertedArray = aadharno.split('').map(Number).reverse();
       var len = invertedArray.length;
       for (var i = 0; i < len; i++) 
      {
              c = d[c][p[(i % 8)][invertedArray[i]]];
      }
      
      
     
      return (c === 0);
}










function myfun2(){

    

    var d = [
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 0, 6, 7, 8, 9, 5], 
        [2, 3, 4, 0, 1, 7, 8, 9, 5, 6], 
        [3, 4, 0, 1, 2, 8, 9, 5, 6, 7], 
        [4, 0, 1, 2, 3, 9, 5, 6, 7, 8], 
        [5, 9, 8, 7, 6, 0, 4, 3, 2, 1], 
        [6, 5, 9, 8, 7, 1, 0, 4, 3, 2], 
        [7, 6, 5, 9, 8, 2, 1, 0, 4, 3], 
        [8, 7, 6, 5, 9, 3, 2, 1, 0, 4], 
        [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
      ]
      var p = [
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 
        [1, 5, 7, 6, 2, 8, 3, 0, 9, 4], 
        [5, 8, 0, 3, 7, 9, 6, 1, 4, 2], 
        [8, 9, 1, 6, 0, 4, 3, 5, 2, 7], 
        [9, 4, 5, 3, 1, 2, 6, 8, 7, 0], 
        [4, 2, 8, 6, 5, 7, 3, 9, 0, 1], 
        [2, 7, 9, 3, 8, 0, 6, 4, 1, 5], 
        [7, 0, 4, 6, 9, 1, 3, 2, 5, 8]
      ]
    var a = document.getElementById("mobile").value;
    var b = document.getElementById("mobile_alt").value;
    var aadharno =  document.getElementById("aadhar").value;
    var panVal =  document.getElementById("pancard").value;

    var name =  document.getElementById("name").value;
    var fathername =  document.getElementById("fathername").value;
    var dateplaceholder =  document.getElementById("dateplaceholder").value;
    var education =  document.getElementById("education").value;
    var occupation =  document.getElementById("occupation").value;
    var residential =  document.getElementById("residential").value;
    var house =  document.getElementById("house").value;
    var street =  document.getElementById("street").value;
    var block =  document.getElementById("block").value;
    var distric =  document.getElementById("distric").value;
    var state =  document.getElementById("state").value;
    var email =  document.getElementById("email").value;
    var message =  document.getElementById("message").value;


    const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;

    var regpan = /^([a-zA-Z]){5}([0-9]){4}([a-zA-Z]){1}?$/;

    if(message==""){
        notie.alert({ type: 'warning',position: 'bottom',text: 'Please tell us something!' })
        document.getElementById("message").focus();
         return false;
    }
    if(!(re.test(email))){
        notie.alert({ type: 'warning',position: 'bottom',text: 'Please enter correct email address!' })
        document.getElementById("email").focus();
         return false;
    }
    if(email==""){
        notie.alert({ type: 'warning',position: 'bottom',text: 'Please enter your email address!' })
        document.getElementById("email").focus();
         return false;
    }
    if(state==""){
        notie.alert({ type: 'warning',position: 'bottom',text: 'Please enter your state!' })
        document.getElementById("state").focus();
         return false;
    }
    if(distric==""){
        notie.alert({ type: 'warning',position: 'bottom',text: 'Please enter your distric!' })
        document.getElementById("distric").focus();
         return false;
    }
    if(block==""){
        notie.alert({ type: 'warning',position: 'bottom',text: 'Please enter your block!' })
        document.getElementById("block").focus();
         return false;
    }
    if(street==""){
        notie.alert({ type: 'warning',position: 'bottom',text: 'Please enter your street!' })
        document.getElementById("street").focus();
         return false;
    }

    if(name==""){
        notie.alert({ type: 'warning',position: 'bottom',text: 'Please enter your name!' })
        document.getElementById("name").focus();
         return false;
    }

    if(fathername==""){
        notie.alert({ type: 'warning',position: 'bottom',text: 'Please enter your last name!' })
        document.getElementById("fathername").focus();
         return false;
    }

    if(dateplaceholder==""){
        notie.alert({ type: 'warning',position: 'bottom',text: 'Please enter choose your date of birth' })
        document.getElementById("dateplaceholder").focus();
         return false;
    }

    if(education==""){
        notie.alert({ type: 'warning',position: 'bottom',text: 'Please enter choose your education!' })
        document.getElementById("education").focus();
         return false;
    }
    if(occupation==""){
        notie.alert({ type: 'warning',position: 'bottom',text: 'Please enter choose your occupation!' })
        document.getElementById("occupation").focus();
         return false;
    }

    if(residential==""){
        notie.alert({ type: 'warning',position: 'bottom',text: 'Please enter choose your residential address!' })
        document.getElementById("residential").focus();
         return false;
    }

    if(house==""){
        notie.alert({ type: 'warning',position: 'bottom',text: 'Please enter choose your house number!' })
        document.getElementById("house").focus();
         return false;
    }



    if(document.getElementById("mobile").value == document.getElementById("mobile_alt").value) {
        document.getElementById("mobile_alt").value="";
        notie.alert({ type: 'warning',position: 'bottom',text: 'Please enter the different Mobile Number!' })
        document.getElementById("mobile_alt").focus();
        return false;
    }
    
    if(!(regpan.test(panVal))){
        document.getElementById("pancard").value="";
        notie.alert({ type: 'warning',position: 'bottom',text: 'Pancard Number is invalid!' })
        document.getElementById("pancard").focus();
         return false;
    } 
    if (isNaN(a)){
        document.getElementById("mobile").value="";
        notie.alert({ type: 'warning',position: 'bottom',text: 'Please enter correct mobile number!' })
        document.getElementById("mobile").focus();
         return false;
    }
    if(a.length<10){
        document.getElementById("mobile").value="";
        notie.alert({ type: 'warning',position: 'bottom',text: 'Mobile Number can not be less than 10 digits' })
          document.getElementById("mobile").focus();
         return false;
    }
    if(a.length>10){
        document.getElementById("mobile").value="";
        notie.alert({ type: 'warning',position: 'bottom',text: 'Mobile Number can not be more than 10 digits' })
        document.getElementById("mobile").focus();
         return false;
    }
    if (isNaN(b)){
        document.getElementById("mobile_alt").value="";
        notie.alert({ type: 'warning',position: 'bottom',text: 'Mobile Number must contain digits only!' })
        document.getElementById("mobile_alt").focus();
        return false;
    }
    if(b.length<10){
        document.getElementById("mobile_alt").value="";
        notie.alert({ type: 'warning',position: 'bottom',text: 'Mobile Number can not be less than 10 digits' })
        document.getElementById("mobile_alt").focus();
        return false;
    }
    if(b.length>10){
        document.getElementById("mobile_alt").value="";
        notie.alert({ type: 'warning',position: 'bottom',text: 'Mobile Number can not be more than 10 digits' })
        document.getElementById("mobile_alt").focus();
        return false;
    }
  
   
    if(isNaN(aadharno))
    {
        document.getElementById("aadhar").value="";
        notie.alert({ type: 'warning',position: 'bottom',text: 'Aadhar Number can contain numbers only!' })
        document.getElementById("aadhar").focus();
         return false;
    }
   

   
    if(aadharno.length!=12)
    {   
        document.getElementById("aadhar").value="";
        notie.alert({ type: 'warning',position: 'bottom',text: 'Aadhar Number can contain 12 digits only!' })
        document.getElementById("aadhar").focus();
        return false;
    }
   
   
   
   
      var c = 0;
      var invertedArray = aadharno.split('').map(Number).reverse();
       var len = invertedArray.length;
       for (var i = 0; i < len; i++) 
      {
              c = d[c][p[(i % 8)][invertedArray[i]]];
      }
      
      
     
      return (c === 0);
}



function fun(){
    var email = document.getElementById("email").value;
    const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;


    if(email==""){

        notie.alert({ type: 'warning',position: 'bottom',text: 'Please enter your email address!' })
        document.getElementById("email").focus();
        return false;
    }
    if(!(re.test(email))){
        notie.alert({ type: 'warning',position: 'bottom',text: 'Please enter correct email address!' })
        document.getElementById("email").focus();
         return false;
    }

    
}