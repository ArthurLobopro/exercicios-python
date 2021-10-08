const path = require('path')
const fs = require('fs')

const dirPath = path.resolve(__dirname, "Desafios")

const desafiosDir = fs.readdirSync(dirPath, {withFileTypes : true})

const folders = desafiosDir.filter( fileOrDir => !fileOrDir.isFile())

folders.forEach( folder => {
    const readmePath = path.resolve(dirPath, folder.name, 'README.md')
    if(fs.existsSync(readmePath)){
        const content = fs.readFileSync(readmePath)
        const newContent = content.toString().replace('**Enunciado:** ', "## Enunciado: \n\n")
        fs.writeFileSync(readmePath, newContent, { encoding: 'utf-8'})
    }
})