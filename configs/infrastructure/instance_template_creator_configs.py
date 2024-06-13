from dataclasses import dataclass, field
from typing import Any
from instance_template_creator import VMType
from omegaconf import SI
@dataclass

class BootDiskConfig:
    project_id: str = "ubuntu-os-cloud"
    name: str = "ubuntu-2204-jammy-v20240607"
    size_gb: int = 50
    labels: Any = SI("${..labels}")



@dataclass
class VMConfig:
    machine_type: str = "n1-standard-1"
    accelerator_count: int = 0
    accelerator_type: str = "nvidia-tesla-t4"
    vm_type: VMType = VMType.STANDARD
    disks: list[str] = field(default_factory= lambda : [])


@dataclass
class VMMetadataConfig:
    instance_group_name : str = SI("${infrastructure.instance_group_creator.name}")
    docker_image: str = SI("${docker_image}")
    zone: str = SI("${infrastructure.zone}")
    python_hash_seed: int = 42
    mlflow_tracking_uri: str = SI("${infrastructure.mlflow.mlflow_internal_tracking_uri}")
    node_count: int = SI("${infrastructure.instance_group_creator.node_count}")
    disks: list[str] = SI("${..vm_config.disks}")


@dataclass
class InstanceTemplateCreatorConfig:
    _target_: str = "instance_template_creator.InstanceTemplateCreator"
    scopes: list[str] = field(default_factory=lambda:[
            "https://www.googleapis.com/auth/cloud-platform",
            "https://www.googleapis.com/auth/cloud.useraccounts.readonly",
            "https://www.googleapis.com/auth/cloudruntimeconfig",
    ])
    network: str = SI("https://www.googleapis.com/compute/v1/projects/${infrastructure.project_id}/global/networks/default")
    subnetwork: str = SI("https://www.googleapis.com/compute/v1/projects/${infrastructure.project_id}/regions/${infrastructure.region}/subnetworks/default")
    startup_script_path: str = SI("scripts/task_runner_startup_script.sh")
    vm_config: VMConfig = VMConfig()
    boot_disk_config: BootDiskConfig = BootDiskConfig()
    vm_metadata_config: VMMetadataConfig = VMMetadataConfig()
    template_name: str = SI("${infrastructure.instance_group_creator.name}")
    project_id: str = SI("${infrastructure.project_id}")
    labels: dict[str,str] = field(default_factory= lambda : {
        "project":"ageless-fire-423616-e1"
    })




