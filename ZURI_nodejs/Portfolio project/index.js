const path = require('path'); //import path module
const  fs = require('fs'); // import filesystem module
const http = require("http"); //import http module


const server = http.createServer((req,res) => {
    let FilePath = path.join(__dirname, 'public', req.url === '/' ? 'home.html' : req.url)
    let contentType = getContentType(FilePath) || 'text/html'
    let emptyPagePath = path.join(__dirname, 'public', '404.html')
    
    fs.readFile(FilePath,'utf8', (err, content) => {
        if(err){
            if(err.code === 'ENOENT'){
                fs.readFile(emptyPagePath, 'utf8', (err, content) =>{
                    res.writeHead(200, {'Content-Type': contentType});
                    res.end(content)
                })
            }else {
                res.writeHead(500)
                res.end("server error")
            }
        }

        if(!err){
            res.writeHead(200, {'Content-Type' : contentType})
            res.end(content)
        }
           
    })
})

//get content type dynamically

const getContentType = (FilePath) => {
    let extname = path.extname(FilePath)
    if(extname === '.js') {
        return 'text/javascript'
    }
    if(extname === '.css') {
        return 'text/css'
    }
    if(extname === '.png') {
        return 'image/png'
    }
    if(extname === '.jpg') {
        return 'image/jpg'
    }
}
const port = 4000

server.listen(port, () => {
    console.log(`server is running on port ${port}`)
})