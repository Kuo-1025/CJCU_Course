document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('registerForm');
    const usernameInput = form.querySelector('#username');

    form.addEventListener('submit', async function(event) {
        const username = usernameInput.value;
        const inputP4sswd = form.querySelector('#password');
        const inputCheckP4sswd = document.querySelector('#checkpassword');

        if (username) {
            await checkUsername(username);
        }

        /*const userGender = document.getElementById('gender');
        const selectedGender = userGender.value;

        console.log(selectedGender);

        if (selectedGender === 'choose') {
            event.preventDefault();

            showAlert('請選擇性別');
        }*/

        if (inputP4sswd.value !== inputCheckP4sswd.value) {
            event.preventDefault();

            showAlert('密碼與確認密碼不一致！');
        }
    });

    usernameInput.addEventListener('blur', async function() {
        const username = usernameInput.value;

        if (username) {
            await checkUsername(username);
        }
    });

    async function checkUsername(username) {
        fetch(`/check_username/${username}`)
            .then(response => response.json())
            .then(data => {
                const message = data.message;
                console.log(message);

                if (data.message !== '該用戶名尚未被使用') {
                    showAlert(data.message);
                }
        })
        .catch(error => console.error('error：', error));
    }

    function showAlert(message) {
        Swal.fire({
            icon: "error",
            title: "非常抱歉",
            text: message
        });
    }
});