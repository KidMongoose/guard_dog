$(() => {
    $('#clipboardPasswd').on('click', (e) => {
         e.preventDefault()
         var password = document.getElementById('generated-password').innerHTML
         navigator.clipboard.writeText(password)     
    })

    $('#personal-info button').on('click', (e) => {
        e.preventDefault()
        let overlay = document.createElement('div')
        overlay.setAttribute('class', 'overlay')
        let modal = document.createElement('div')
        modal.setAttribute('class', 'modal')
        overlay.appendChild(modal)
        let p = document.createElement('p')
        let pText = document.createTextNode('Personal info saved')
        p.appendChild(pText)
        modal.appendChild(p)
        var body = document.querySelector("body");
        body.appendChild(overlay)

        setTimeout(() => {
           $('.overlay').hide()
        }, 1500)

         
    })

})                   