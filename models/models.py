from odoo import models, fields, api
from datetime import datetime

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patient'

    name = fields.Char(string="Patient Name", required=True)
    date_of_birth = fields.Date(string="Date of Birth")
    age = fields.Integer(string="Age", compute="_compute_age", store=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender")
    disease = fields.Char(string="Disease")
    doctor_id = fields.Many2one('hospital.doctor', string="Doctor")
    notes = fields.Html(string="Notes")
    is_discharged = fields.Boolean(string="Discharged")
    medical_records = fields.One2many('hospital.record', 'patient_id', string="Medical Records")
    attachment = fields.Binary(string="Document Attachment")

    @api.onchange('date_of_birth')
    def _onchange_date_of_birth(self):
        if self.date_of_birth:
            today = datetime.today()
            birth_date = fields.Date.from_string(self.date_of_birth)
            self.age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        else:
            self.age = 0

    @api.depends('date_of_birth')
    def _compute_age(self):
        for record in self:
            if record.date_of_birth:
                today = datetime.today()
                birth_date = fields.Date.from_string(record.date_of_birth)
                record.age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
            else:
                record.age = 0

class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'Hospital Doctor'

    name = fields.Char(string="Doctor Name", required=True)
    specialty = fields.Char(string="Specialty")
    phone = fields.Char(string="Phone Number")

class HospitalRecord(models.Model):
    _name = 'hospital.record'
    _description = 'Medical Record'

    name = fields.Char(string="Record Name", required=True)
    patient_id = fields.Many2one('hospital.patient', string="Patient", required=True)
    description = fields.Text(string="Description")
