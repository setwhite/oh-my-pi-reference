<guidelines>
  <section name="Python 规范">
    <rule>
      <when>安装或管理包时</when>
      <do>使用 uv</do>
      <dont>使用 pip</dont>
    </rule>
    <rule>
      <when>定义函数签名、类属性或数据类字段时</when>
      <do>编写完整的类型标注</do>
      <dont>省略类型标注</dont>
    </rule>
  </section>

  <section name="KISS 原则">
    <rule>
      <when>编写代码、文档、或做任何工程决策时</when>
      <do>保持简洁——只做任务所需的最小改动，不加未要求的灵活性</do>
      <dont>过度设计、随意推测、画蛇添足</dont>
    </rule>
  </section>

  <section name="语言规范">
    <rule>
      <when>编写注释、Docstrings、设计文档或提交信息时</when>
      <do>强制使用中文</do>
      <dont>使用任何非中文语言、除非是专业术语</dont>
    </rule>
  </section>

  <section name="代码硬性上限">
    <rule>
      <when>编写函数或方法时</when>
      <do>函数体 ≤ 50 行；超过则拆分</do>
      <dont>放任函数无限增长</dont>
    </rule>
    <rule>
      <when>编写任何源文件时</when>
      <do>文件 ≤ 300 行；超过则拆模块</do>
      <dont>把所有逻辑堆进单文件</dont>
    </rule>
    <rule>
      <when>编写控制流时</when>
      <do>嵌套深度 ≤ 3 层；超过则提取函数或提前 return</do>
      <dont>深层嵌套</dont>
    </rule>
    <rule>
      <when>定义函数签名时</when>
      <do>位置参数 ≤ 3 个；超过则改用对象/数据类传参</do>
      <dont>参数列表无限扩张</dont>
    </rule>
    <rule>
      <when>编写条件分支或循环时</when>
      <do>圈复杂度 ≤ 10；超过则拆分逻辑</do>
      <dont>写出不可测试的意大利面条</dont>
    </rule>
    <rule>
      <when>编写任何字面量时</when>
      <do>用命名常量代替魔法数字</do>
      <dont>裸写数字字面量（0、1、-1 等公认语义值除外）</dont>
    </rule>
  </section>

  <section name="代码维护">
    <rule>
      <when>修改现有代码时</when>
      <do>确保每一行 Diff 都直接追溯到当前需求</do>
      <dont>附带无关的优化、注释或格式修改、重构未损坏的逻辑</dont>
    </rule>
    <rule>
      <when>既有代码基础上工作时</when>
      <do>强制沿用现有代码风格——命名、格式、设计模式</do>
      <dont>擅自更改代码风格</dont>
    </rule>
    <rule>
      <when>清理本次改动产生的死代码时</when>
      <do>只删除因本次改动而废弃的依赖、变量或函数</do>
      <dont>擅自删除历史遗留的死代码；如发现，可以提示用户，但严禁自行删除</dont>
    </rule>
  </section>

  <section name="交付闸门">
    <rule>
      <when>声明任务完成、准备 commit、或准备 push 之前</when>
      <do>
        逐条确认以下四道闸门全部通过：
        1. 已完成与本次改动直接相关的验证，并如实报告结果
        2. 已通过该任务对应的测试等级（见 tdd skill 分流判定）
        3. 若仓库或项目有更严格的验证要求，以仓库为准
        4. 若关键验证无法执行，明确说明原因，并降低完成度表述
      </do>
      <dont>
        声称「完成」「通过」「没问题」但未实际运行验证
        跳过验证后仍以「已完成」交差
      </dont>
    </rule>
  </section>

</guidelines>
