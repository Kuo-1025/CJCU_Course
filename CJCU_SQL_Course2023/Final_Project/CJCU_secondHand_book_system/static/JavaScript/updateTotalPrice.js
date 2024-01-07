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