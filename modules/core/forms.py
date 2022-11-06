from wtforms_alchemy import Unique,ModelForm
import json
from flask_wtf import FlaskForm
from wtforms import HiddenField,BooleanField,FieldList,StringField,MultipleFileField

class BaseForm(FlaskForm,ModelForm):
    obj_data = None
    id_obj = HiddenField()
    ativo = BooleanField('Ativo',default = True)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.obj_data = kwargs.get('obj',None)
        if 'obj' in kwargs:
            obj = kwargs['obj']
            if obj:
                self.id_obj.data = self.obj_data.id

class BasePesquisaForm(FlaskForm):
    ativo = BooleanField('Ativo',default = False)
    nome = StringField('Nome',render_kw={'maxlength':'255'})