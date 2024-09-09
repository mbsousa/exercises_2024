const frm = document.querySelector("form")
const resp = document.querySelector("h3")

const emails = []


frm.addEventListener("submit", (e) => {
    e.preventDefault()
    const n = frm.inNome.value
    const email = frm.inEmail.value

    i = -1
   if (emails.length!==0) {
    for (const e of emails){
        if (e.nome === n) {
            i = index /* Marca o indice do nome existente */
            break
        }
        }
    }

   if (i===-1){
    const obj=({'nome':n, 'email':email})
    emails.push(obj)
    resp.innerText=`O nome ${obj.nome} foi incluido com sucesso!`
   }
   else {
    resp.innerText=`O nome ${obj.nome} já está cadastrado.`
   }

})


frm.btProcurar.addEventListener("click", () => {

    const n = frm.inNome.value

    if (!frm.checkValidity()) {
        alert("Informe o nome a ser cadastrado!")
        frm.inNome.focus()
        return
    }

    let i = -1

    if (emails.length!==0){
        for (const e of emails){
            const {nome,email} = e 
            if (nome == n){
                i=1
                break
            }
        }    
    }
    
    if (i==-1){
        resp.innerText=`O nome ${n} foi incluido com sucesso!`
    }
    else {
        resp.innerText=`O nome ${n} já está cadastrado!Tente outro nome!`
    }

})

frm.btListar.addEventListener("click", () => {
    if (emails.length === 0) {
        resp.textContent = "Nenhum cadastro encontrado!"
        return
    }

    let lista = "Lista de nomes e emails cadastrados:"
    for (let i = 0; i < emails.length; i++) {
        lista += `\n${emails[i].nome} - \n${emails[i].email}\n`
    }

    resp.textContent = lista
})
