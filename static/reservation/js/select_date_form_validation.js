function checkService() {
    var errorServiceAlert = document.getElementById("empty-service-alert");

    var service = document.getElementById("id_service").value;
    if (service) {
        errorServiceAlert.style.display = "none";
        document.getElementById("submit-btn").disabled = false;

    } else {
        errorServiceAlert.textContent = "لطفا سرویس را هم پر کنید";
        errorServiceAlert.style.display = "block";
        document.getElementById("submit-btn").disabled = true;
    }
}


document.addEventListener("DOMContentLoaded", function () {
    var form = document.querySelector("form");
    var errorAlert = document.getElementById("error-alert");

    form.addEventListener("submit", function (event) {
        var service = form.querySelector("select[name='service']").value;
        var date = form.querySelector("input[name='date']").value;

        if (!service || !date) {
            errorAlert.textContent = "لطفاً هر دو فیلد سرویس و تاریخ را پر کنید.";
            errorAlert.style.display = "block";
            event.preventDefault(); // این کد از ارسال فرم جلوگیری می‌کند
        } else {

            errorAlert.style.display = "none";
        }
    });
});


