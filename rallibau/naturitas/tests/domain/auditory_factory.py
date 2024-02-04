from datetime import datetime

from factory import DictFactory

from naturitas.domain.Auditory import Auditory


class AuditoryFactory(DictFactory):
    change_date = datetime.now()
    user = "foo_user"
    model_name = "foo_model"
    model_instance_id = 1
    data_before_change = "{'foo':'foo'}"
    data_after_change = "{'foo':'foo'}"

    class Meta:
        model = Auditory
