let display=document.getElementById('screen-id');
let buttons=Array.from(document.getElementsByClassName('btns'));
buttons.map( buttons =>{
    buttons.addEventListener('click',(e)=>{
        switch(e.target.innerText){
            case 'AC':
                display.innerText='';
                break;
            case 'X':
                display.innerText=display.innerText.slice(0,-1);
                break;
            case '=':
                try{
                    display.innerText=display.innerText+"\n"+"\n"+"="+eval(display.innerText);
                }catch{
                    display.innerText='Error';
                }
                
                break;
            default:
                display.innerText+=e.target.innerText;
        }
    })
})
