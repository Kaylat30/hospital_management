from odoo import models, fields

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patient'

    name = fields.Char(string="Patient Name", required=True)
    age = fields.Integer(string="Age")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender")
    disease = fields.Char(string="Disease")
    # doctor_id = fields.Many2one('hospital.doctor', string="Doctor")
    notes = fields.Html(string="Notes")
    is_discharged = fields.Boolean(string="Discharged")
    # medical_records = fields.One2many('hospital.record', 'patient_id', string="Medical Records")
    attachment = fields.Binary(string="Document Attachment")
