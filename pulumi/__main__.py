"""A Python Pulumi program for a Vercel OpenAI chatbot"""

import pulumi
import pulumiverse_vercel as vercel

# Retrieve configuration values
config = pulumi.Config()
openai_api_key = config.require_secret("openai_api_key")
git_repo = config.require("git_repo")

# Create a Vercel project
project = vercel.Project("vercel-chatbot-project",
    framework="nextjs",
    git_repository=vercel.ProjectGitRepositoryArgs(
        repo=git_repo,
        type="github",
    ),
    environments=[vercel.ProjectEnvironmentArgs( # Passing OpenAI api key as an environment variable
        key="OPENAI_API_KEY",
        value=openai_api_key,
        targets=["production", "preview", "development"],
    )]
)

# Create a Vercel deployment
deployment = vercel.Deployment("vercel-chatbot-deployment",
    project_id=project.id,
    production=True,
    ref="main",
)

# Export the URL of the app
pulumi.export("url", pulumi.Output.concat("http://", deployment.url))