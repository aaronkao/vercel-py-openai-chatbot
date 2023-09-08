"""A Python Pulumi program for a Vercel OpenAI Chatbot"""

import pulumi
import pulumiverse_vercel as vercel

config = pulumi.Config()
openai_api_key = config.require_secret("openai_api_key")
git_repo = config.require("git_repo")


project = vercel.Project("vercel-chatbot-project",
    framework="nextjs",
    git_repository=vercel.ProjectGitRepositoryArgs(
        repo=git_repo,
        type="github",
    ),
    environments=[vercel.ProjectEnvironmentArgs(
        key="OPENAI_API_KEY",
        value=openai_api_key,
        targets=["production", "preview", "development"],
    )]
)

deployment = vercel.Deployment("vercel-chatbot-deployment",
    project_id=project.id,
    production=True,
    ref="main",
)    