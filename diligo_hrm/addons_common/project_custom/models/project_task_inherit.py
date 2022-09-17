from odoo import api, fields, models
from odoo.exceptions import ValidationError
import datetime
# import time

class ProjectMission(models.Model):

    _inherit = "project.task"

    _sql_constraints = [
        ('check_date',
         'CHECK (date_start <= date_end)',
         'Rule date start can not larger than date end!'),
    ]

    description_detail = fields.Text(string='Mission detail',)
    # dev_id = fields.Many2one('hr.employee', string='Dev')
    # tester_id = fields.Many2one('hr.employee', string='Tester')
    # task_recipient_ids = fields.Many2many('', string='Task recipient')
    note_bug = fields.Text(string='Note bug')
    mission_status = fields.Text(string='Mission status')
    # is_dev= fields.Boolean(string='Is dev or not', default=False)

    date_start = fields.Datetime(string='Start Date')
    date_deadline = fields.Date(string='Deadline', index=True, copy=False, tracking=True, task_dependency_tracking=True,
                                help='Date deadline must larger than date end')
    date_receive = fields.Datetime(string='Date receive', default=fields.Datetime.now)

    child_2_ids = fields.One2many('project.task', 'parent_id',
                                    help='Use to view tab')
    # child_dev_ids= fields.One2many('project.task', 'parent_id', string='Child dev', domain=[('is_dev', '=', True)], help='Use to view dev tab')
    # child_tester_ids = fields.One2many('project.task', 'parent_id', string='Child tester',
    #                                 help='Use to view tester tab')  #domain=[('is_dev', '=', False)],


    # ràng buộc ngày hạn chót phải không được nhỏ hơn ngày kết thúc kế hoạch
    @api.constrains('date_end', 'date_deadline')
    def _constrains_date_end_and_date_dealine(self):
        for rec in self:
            if rec.date_end and rec.date_deadline:
                if rec.date_deadline < rec.date_end.date():
                    raise ValidationError("Date deadline is not less than end date")


    # @api.model
    # def create(self, vals):
    #     if 'date_end' and 'date_deadline' in vals:
    #         print('tao date end and date deadline')
    #         if vals['date_deadline'] < vals['date_end'].date():
    #             raise ValidationError("Date deadline is not less than end date")
    #
    #     return super(ProjectMission, self).create(vals)
    #
    # def write(self, vals):
    #     print('self.project_mission_ids.ids', self.project_mission_ids.ids)
    #     if 'project_mission_ids' in vals:
    #         print(vals['project_mission_ids'])
    #         self.env['project.test.detail'].create({
    #             # 'mission_id': vals['project_mission_ids'],
    #                                                 'project_task_id': self.id
    #                                                 })
    #         self.env['res.users'].create({
    #             'name': 'Marc Demo',
    #             'email': 'mark.brown23@example.com',
    #             'image_1920': False,
    #             'create_date': '2015-11-12 00:00:00',
    #             'login': 'demo_1',
    #             'password': 'demo_1'
    #         })
    #
    #     return super(ProjectMission, self).write(vals)