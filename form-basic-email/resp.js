const frm = document.querySelector("form")
const resp = document.querySelector("h3")

const nomes = []
const emails = []


frm.addEventListener("submit", (e) => {
    e.preventDefault()
    const nome = frm.inNome.value
    const email = frm.inEmail.value
    const i = nomes.indexOf(nome)
    const em = emails.indexOf(email)

    if (i !== -1) {
        alert("Nome já cadastrado!")
        frm.inNome.focus()
        return
    }

    if (em !== -1) {
        alert("Email já cadastrado!")
        frm.inNome.focus()
        return
    }

    nomes.push(nome)
    emails.push(email)
    alert("Cadastrado realizado com sucesso!")
    frm.reset()
    frm.inNome.focus()

})


frm.btProcurar.addEventListener("click", () => {
    if (!frm.checkValidity()) {
        alert("Informe o nome a ser cadastrado!")
        frm.inNome.focus()
        return
    }

    const i = nomes.indexOf(nome)

            if (i !== -1) {
                resp.textContent = `Nome: ${nomes[i]} - Email: ${emails[i]}`
            } else {
                resp.textContent = "Nome não encontrado!"
            }
        
})

frm.btListar.addEventListener("click", () => {
    if (nomes.length === 0) {
        resp.textContent = "Nenhum cadastro encontrado!"
        return
    }

    let lista = "Lista de nomes e emails cadastrados:"
    for (let i = 0; i < nomes.length; i++) {
        lista += `\n${nomes[i]} - \n${emails[i]}\n`
    }

    resp.textContent = lista
})