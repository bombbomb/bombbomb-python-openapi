# coding: utf-8

"""
    BombBomb

    We make it easy to build relationships using simple videos.

    OpenAPI spec version: 2.0.25797
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from __future__ import absolute_import

# import models into sdk package
from .models.bb_web_hook import BBWebHook
from .models.curriculum import Curriculum
from .models.curriculum_user_progress import CurriculumUserProgress
from .models.curriculum_with_progress import CurriculumWithProgress
from .models.hosted_doc import HostedDoc
from .models.inline_response_200 import InlineResponse200
from .models.inline_response_200_items import InlineResponse200Items
from .models.jericho_configuration import JerichoConfiguration
from .models.jericho_performance import JerichoPerformance
from .models.o_auth_client import OAuthClient
from .models.prompt_bot import PromptBot
from .models.sign_upload_request import SignUploadRequest
from .models.sign_upload_response import SignUploadResponse
from .models.string import String
from .models.team_public_representation import TeamPublicRepresentation
from .models.video_email_prompt import VideoEmailPrompt
from .models.video_encoding_status_response import VideoEncodingStatusResponse
from .models.video_public_representation import VideoPublicRepresentation
from .models.video_recorder_method_response import VideoRecorderMethodResponse

# import apis into sdk package
from .apis.accounts_api import AccountsApi
from .apis.automations_api import AutomationsApi
from .apis.contacts_api import ContactsApi
from .apis.curriculum_api import CurriculumApi
from .apis.emails_api import EmailsApi
from .apis.files_api import FilesApi
from .apis.integrations_api import IntegrationsApi
from .apis.lists_api import ListsApi
from .apis.orders_api import OrdersApi
from .apis.prompts_api import PromptsApi
from .apis.socials_api import SocialsApi
from .apis.teams_api import TeamsApi
from .apis.utilities_api import UtilitiesApi
from .apis.videos_api import VideosApi
from .apis.webhooks_api import WebhooksApi

# import ApiClient
from .api_client import ApiClient

from .configuration import Configuration

configuration = Configuration()
