function checkService() {
    
    var selectedService = document.getElementById("id_service").value;
    console.log(selectedService);
    var serviceInputs = document.querySelectorAll("input[name='service']");
    for (var i = 0; i < serviceInputs.length; i++) {
        serviceInputs[i].value = selectedService;
    }
}
