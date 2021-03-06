# Copyright (C) Linaro Limited 2017
# Author: Milo Casagrande <milo.casagrande@linaro.org>
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free
# Software Foundation; either version 2.1 of the License, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this library; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA

"""Create the error reports."""


import utils.report.common as rcommon


MULTIPLE_EMAILS_SUBJECT = \
    u"Duplicate email trigger received for {job} - {git_branch} - {kernel}"


def create_duplicate_email_report(data):
    """Create the email report for duplicated trigger emails.

    When we receive multiple triggers for the same job-kernel, send an error
    email.
    Only a TXT one will be created.

    :param data: The data for the email.
    :type dict
    :return The txt and html body, and the subject string.
    """
    subject_str = MULTIPLE_EMAILS_SUBJECT.format(**data)
    txt_body = rcommon.create_txt_email("multiple_emails.txt", **data)

    return txt_body, None, subject_str
