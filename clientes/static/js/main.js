(function () {

    const btnEliminacion = document.querySelectorAll('.btnEliminacion');
    
    btnEliminacion.forEach(btn => {
        btn.addEventListener('click', (e) => {
            // const confirmacion = confirm("¿Seguro de eliminar el cliente?");
            // if (!confirmacion) {
            //     e.preventDefault();
            // }
            e.preventDefault();
            Swal.fire({
                title: "¿Confirmar la eliminación del cliente?",
                showCancelButton: true,
                confirmButtonText: "Eliminar",
                confirmButtonColor: "#bf616a",
                cancelButtonColor: "#4c566a",
                cancelButtonText: "Cancelar",
                backdrop: true,
                showLoaderConfirm: true,
                preConfirm:()=>{
                    location.href = e.target.href
                },
                allowOutsideClick: () => false,
                allowScapeKey: () => false
            })
        })
    })
})();


