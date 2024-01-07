function searchProducts() {
    const keyword = document.getElementById('searchProducts').value;

    if (String(keyword).length == 0) {
        return;
    }

    fetch(`/search?keyword=${keyword}`)
        .then(response => response.json())
        .then(data => {
            const productsList = document.getElementById('productsList');
            productsList.innerHTML = '';

            for (product of data.productsList) {
                const cardContainer = document.createElement('div');
                cardContainer.className = 'col-md-4 mb-4';

                const card = document.createElement('div');
                card.className = 'card';

                const cardBody = document.createElement('div');
                cardBody.className = 'card-body';

                const title = document.createElement('h5');
                title.className = 'card-title';
                title.textContent = product.B_name;

                const author = document.createElement('p');
                author.className = 'card-text';
                author.textContent = `作者: ${product.B_author}`;

                const price = document.createElement('p');
                price.className = 'card-text';
                price.textContent = `價格: ${product.B_price} 元`;

                const detailLink = document.createElement('a');
                detailLink.href = `/show_product_detail/${product.B_id}`;
                detailLink.className = 'card-link';
                detailLink.textContent = '查看詳情';

                cardBody.appendChild(title);
                cardBody.appendChild(author);
                cardBody.appendChild(price);
                cardBody.appendChild(detailLink);

                card.appendChild(cardBody);
                cardContainer.appendChild(card);

                productsList.appendChild(cardContainer);
            }
        })
        .catch(error => console.error('Error searching products:', error));
}