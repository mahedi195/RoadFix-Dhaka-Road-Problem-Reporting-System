
const inputPhoto=document.querySelector("input[name='uploaded_photo']");


inputPhoto.addEventListener('change',function()
{
    const image=inputPhoto.files[0];
    if(image)
    {
        const showPhoto=document.querySelector('.showPhoto')
        showPhoto.src=URL.createObjectURL(image)
        showPhoto.style.display='block'

    }

})