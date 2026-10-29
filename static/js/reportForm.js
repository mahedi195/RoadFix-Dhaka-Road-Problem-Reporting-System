


const inputPhoto=document.querySelector("input[name='uploaded_photo']");


const showPhoto=document.querySelector('.showPhoto')



inputPhoto.addEventListener('change',function()
{
    const image=inputPhoto.files[0];
    if(image)
    {
        showPhoto.src=URL.createObjectURL(image)
        showPhoto.style.display='block'

    }

})