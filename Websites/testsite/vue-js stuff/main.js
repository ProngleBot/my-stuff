function cheeser(){
    var name = document.getElementById('name').value;
    var cheese = document.getElementById('cheese').value;
    
    if (cheese == 'i dont like cheese'){
        var result = "ew get away from me "+name;
        document.getElementById('response').innerHTML= result;
    }
    else if(cheese == void(0)) {
        var result = "check if you have entered everything correctly"
        document.getElementById('response').innerHTML= result;
    }
    else {
        var result = "I'm impressed "+name+" i quite enjoy "+cheese+" too";
        document.getElementById('response').innerHTML = result;
    }
}