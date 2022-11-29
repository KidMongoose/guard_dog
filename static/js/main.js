$(() => {
    $('#clipboardPasswd').on('click', (e) => {
         e.preventDefault()
         var password = document.getElementById('generated-password').innerHTML
         navigator.clipboard.writeText(password) 
        
    })

})                   