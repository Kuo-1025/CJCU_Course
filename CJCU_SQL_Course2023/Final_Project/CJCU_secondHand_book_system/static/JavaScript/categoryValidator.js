document.addEventListener('DOMContentLoaded', function() {
    form = document.getElementById('addProductForm');

    form.addEventListener('submit', function(event) {
        const categoryDropdown = document.getElementById('category');
        const selectedCategory = categoryDropdown.value;

        console.log(selectedCategory);

        if (selectedCategory === '--- 請選擇類別 ---') {
            event.preventDefault();

            showAlert('請選擇商品分類');
        }
    })
    
    function showAlert(message) {
        Swal.fire({
            icon: "error",
            title: "非常抱歉",
            text: message
        });
    }
});