
from dataclasses import dataclass

from configs.infrastructure.instance_template_creator_configs import InstanceTemplateCreatorConfig
from omegaconf import SI

@dataclass
class InstanceGroupCreatorConfig:
    _target_: str = "instance_group_creator.InstanceGroupCreator"
    instance_template_creator: InstanceTemplateCreatorConfig = InstanceTemplateCreatorConfig()
    #name: str = SI("${infrastructure.mlflow.experiment_name}-${infrastructure.mlflow.run_name}-${now:%y$m%d%H%M%S}")
    name: str = "test"
    node_count: int = 1
    project_id: str = SI("${infrastructure.project_id}")
    zone: str = SI("${infrastructure.zone}")
    region: str = SI("${infrastructure.region}")
