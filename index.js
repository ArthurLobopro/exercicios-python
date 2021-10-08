const path = require('path')
const fs = require('fs')

const dirPath = path.resolve(__dirname, "Desafios")

const desafiosDir = fs.readdirSync(dirPath, {withFileTypes : true})

const files = desafiosDir.filter( fileOrDir => fileOrDir.isFile()).filter( file => path.extname(file.name) == '.py')

files.forEach( file => {
    const name = file.name.replace('.py', '')
    const newDirPath = path.resolve(dirPath, name)

    const oldPath = path.resolve(dirPath, file.name)
    const newPath = path.resolve(newDirPath, file.name)
    fs.mkdirSync(newDirPath)
    fs.renameSync(oldPath, newPath, err => console.log('deu ruim'))

    const readmePath = path.resolve(newDirPath, 'README.md')
    fs.writeFileSync(readmePath, `# ${name.toUpperCase()}`, { encoding: 'utf-8'})
})