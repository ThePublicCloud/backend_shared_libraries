import hashlib

from pydantic import BaseModel
import hashlib


class NodeDetails(BaseModel):
    name: str
    id: str

    def __str__(self):
        return hashlib.sha256((self.name + self.id).encode()).hexdigest()


class RegistrationDetails(BaseModel):
    k8s_ip: str
    k8s_port: int
    k8s_token: str

    vpn_ip: str
    vpn_port: int
    vpn_token: str
