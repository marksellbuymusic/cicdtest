module.exports = {
  apps: [
    {
      name: "cicd-frontend",
      script: "npm start",
      watch: true,
      exec_mode: "fork",
      cwd: "/app/", //the directory from which your app will be launched
      args: "", //string containing all arguments passed via CLI to script
      error_file: "/app/log/err.log",
      out_file: "/app/log/out.log",
      ignore_watch: ["node_modules", "/app/log", "/app/.next"],
    },
  ],
};
