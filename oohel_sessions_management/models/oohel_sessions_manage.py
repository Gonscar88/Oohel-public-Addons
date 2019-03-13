# -*- coding: utf-8 -*-
# Created by Oohel at 8/03/19
# Oohel Extra Tools 2019
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
import os
from odoo import fields, models


class OohelSessionsManage(models.TransientModel):
    _name = 'oohel.sessions_manage'

    def delete_all_session_files(self):
        """
        Odoo saves al sessions in separated files with the name of the session_id cookie,
        we delete these files to reset all the sessions
        :return:
        """
        path = "/odoo/.local/share/Odoo/sessions/"
        for filename in os.listdir(path):
            if filename.endswith('.sess'):
                os.unlink(path + str(filename))
