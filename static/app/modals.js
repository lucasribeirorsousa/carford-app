function RETORNA_MODAL_PADRAO(titulo='',txt_btn='Enviar',icon_btn='fas fa-share-square',class_btn='btn-blue',class_modal ='col-6') {
    return  send_sms_modal = $.confirm({
        lazyOpen: true,
        title:titulo,
        theme:'material',
        type: 'dark',
        closeIcon: true,
        columnClass:'col-6',
          buttons:{
            enviar: {
              text: `<i class="${icon_btn}"></i> ${txt_btn}`,
              btnClass: class_btn,
              action: function () {


                return false;
                
          },
        },
        }
    });
  }

