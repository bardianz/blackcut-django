document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".make-done-btn").forEach(button => {
        button.addEventListener("click", function () {
            let reservationId = this.dataset.id;  // دریافت ID از data-id
            let buttonId = this.id;  // دریافت ID دکمه

            fetch("/api/make_done_appointment/", {  // مسیر API را بررسی کنید
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": getCSRFToken()  // برای امنیت لازم است
                },
                body: JSON.stringify({ "appointment_id": reservationId })
            })
            .then(response => response.json())
            .then(data => {
                if (data.message) {
                    alert(data.message);  // نمایش پیام موفقیت
                    document.getElementById(buttonId).innerText = "Done ✅";  // تغییر متن دکمه
                    document.getElementById(buttonId).disabled = true;  // غیرفعال‌سازی دکمه
                }
            })
            .catch(error => console.error("Error:", error));
        });
    });

    document.querySelectorAll(".make-paid-btn").forEach(button => {
        button.addEventListener("click", function () {
            let reservationId = this.dataset.id;
            let buttonId = this.id;

            fetch("/api/make-paid/", {  // مسیر API پرداخت را بررسی کنید
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": getCSRFToken()
                },
                body: JSON.stringify({ "appointment_id": reservationId })
            })
            .then(response => response.json())
            .then(data => {
                if (data.message) {
                    alert(data.message);
                    document.getElementById(buttonId).innerText = "Paid ✅";
                    document.getElementById(buttonId).disabled = true;
                }
            })
            .catch(error => console.error("Error:", error));
        });
    });
});

// تابع دریافت CSRF Token از کوکی
function getCSRFToken() {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        document.cookie.split(";").forEach(cookie => {
            let trimmed = cookie.trim();
            if (trimmed.startsWith("csrftoken=")) {
                cookieValue = trimmed.substring("csrftoken=".length);
            }
        });
    }
    return cookieValue;
}
