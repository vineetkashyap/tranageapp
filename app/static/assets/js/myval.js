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
    if (isNaN(a)){
        document.getElementById("mobile").value="";
        document.getElementById("mobile").placeholder="Invalid Mobile No.";
         return false;
    }
    if(a.length<10){
        document.getElementById("mobile").value="";
          document.getElementById("mobile").placeholder="Mobile number must be 10 digits";
         return false;
    }
    if(a.length>10){
        document.getElementById("mobile").value="";
          document.getElementById("mobile").placeholder="Mobile number must be 10 digits";
         return false;
    }
    if (isNaN(b)){
        document.getElementById("mobile_alt").value="";
        document.getElementById("mobile_alt").placeholder="Invalid Mobile No.";
        return false;
    }
    if(b.length<10){
        document.getElementById("mobile_alt").value="";
        document.getElementById("mobile_alt").placeholder="Mobile number must be 10 digits";
        return false;
    }
    if(b.length>10){
        document.getElementById("mobile_alt").value="";
        document.getElementById("mobile_alt").placeholder="Mobile number must be 10 digits";
        return false;
    }
    if(isNaN(aadharno))
    {
        document.getElementById("aadhar").value="";
        document.getElementById("aadhar").placeholder="Invalid aadhar No.";
         return false;
    }
   

   
    if(aadharno.length!=12)
    {   document.getElementById("aadhar").value="";
        document.getElementById("aadhar").placeholder="Invalid aadhar No.";

    return false;
    }
   
   
   
   
      var c = 0;
      var invertedArray = aadharNumber.split('').map(Number).reverse();
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
    var regpan = /^([a-zA-Z]){5}([0-9]){4}([a-zA-Z]){1}?$/;
    
    if(!(regpan.test(panVal))){
        document.getElementById("pancard").value="";
        document.getElementById("pancard").placeholder="Invalid Pancard No.";
         return false;
    } 
    if (isNaN(a)){
        document.getElementById("mobile").value="";
        document.getElementById("mobile").placeholder="Invalid Mobile No.";
        return false;
    }
    if(a.length<10){
        document.getElementById("mobile").value="";
        document.getElementById("mobile").placeholder="Mobile number must be 10 digits";
        return false;
    }
    if(a.length>10){
        document.getElementById("mobile").value="";
        document.getElementById("mobile").placeholder="Mobile number must be 10 digits";
        return false;
    }
    if (isNaN(b)){
        document.getElementById("mobile_alt").value="";
        document.getElementById("mobile_alt").placeholder="Invalid Mobile No.";
        return false;
    }
    if(b.length<10){
        document.getElementById("mobile_alt").value="";
        document.getElementById("mobile_alt").placeholder="Mobile number must be 10 digits";
        return false;
    }
    if(b.length>10){
        document.getElementById("mobile_alt").value="";
        document.getElementById("mobile_alt").placeholder="Mobile number must be 10 digits";
        return false;
    }
  
   
    if(isNaN(aadharno))
    {
        document.getElementById("aadhar").value="";
        document.getElementById("aadhar").placeholder="Invalid aadhar No.";
         return false;
    }
   

   
    if(aadharno.length!=12)
    {   document.getElementById("aadhar").value="";
        document.getElementById("aadhar").placeholder="Invalid aadhar No.";

    return false;
    }
   
   
   
   
      var c = 0;
      var invertedArray = aadharNumber.split('').map(Number).reverse();
       var len = invertedArray.length;
       for (var i = 0; i < len; i++) 
      {
              c = d[c][p[(i % 8)][invertedArray[i]]];
      }
      
      
     
      return (c === 0);
}
