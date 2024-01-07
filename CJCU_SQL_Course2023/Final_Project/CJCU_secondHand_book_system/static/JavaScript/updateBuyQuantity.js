function updateBuyQuantity(item_id, p_id, action) {
    const quantityInp = document.getElementById(`display-quantity-${item_id}`);
    console.log('hehe');
    let newQuantity = parseInt(quantityInp.textContent);

    if (action === 'decrease') {
        --newQuantity;
    } else if (action === 'increase') {
        ++newQuantity;
    }

    fetch(`/check_quantity/${p_id}/${newQuantity}`, {
        method: 'GET'
    })
        .then(response => response.json())
        .then(data => {
            if (data.success){
                quantityInp.textContent = newQuantity;

                const displayQuantity = document.getElementById(`display-quantity-${item_id}`);
                if (displayQuantity) {
                    displayQuantity.textContent = newQuantity;
                }

                fetch(`/update_quantity/${p_id}/${newQuantity}`, {
                    method:  'POST'
                })
                    .then(response => response.json())
                    .then(data => {
                        if (data.success){
                            console.log('Quantity updates seccessfully', data);
                        } else {
                            showAlert(data.message);
                        }
                    })
                    .catch(error => console.error('Error updating quantity:', error))

                const eachPrice = document.getElementById(`eachPrice-${item_id}`).textContent;
                let totalPrice = document.getElementById(`totalPrice-${item_id}`);
                console.log(parseInt(eachPrice.substring(0, eachPrice.indexOf('元') - 1)) * newQuantity);
                totalPrice.textContent = `${parseInt(eachPrice.substring(0, eachPrice.indexOf('元') - 1)) * newQuantity} 元`;
                console.log('after update totalPrice is', totalPrice.textContent);

                updateTotalPrice();
            } else {
                showAlert('數量超出範圍！');
            }
        })
        .catch(error => console.error('Error checking quantity:', error));
}

function updateTotalPrice() {
    const checkBoxes = document.querySelectorAll('input[name="selected_item[]"]:checked');

    let totalPrice = 0;

    for (checkBox of checkBoxes) {
        const item_id = checkBox.value;
        const item_totalPrice = document.getElementById(`totalPrice-${item_id}`).textContent;

        totalPrice += parseInt(item_totalPrice);
    }

    document.getElementById('totalItemPriceSum').textContent = totalPrice;
}

function showAlert(message) {
    Swal.fire({
        icon: "error",
        title: "非常抱歉",
        text: message
    });
}